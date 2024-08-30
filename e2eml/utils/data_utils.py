from pathlib import Path
from subprocess import CalledProcessError, SubprocessError, check_output, run

from e2eml.utils.utils import get_logger, run_shell_command

DATA_UTILS_LOGGER = get_logger(Path(__file__).name)


def is_dvc_initialized() -> bool:
    return (Path().cwd() / ".dvc").exists()


def initialize_dvc() -> None:
    if is_dvc_initialized():
        DATA_UTILS_LOGGER.info("DVC is already initialized")
        return
    DATA_UTILS_LOGGER.info("Initializing DVC")
    run_shell_command("dvc init")
    run_shell_command("dvc config core.analytics false")
    run_shell_command("dvc config core.autostage true")
    run_shell_command("git add .dvc")
    run_shell_command("git commit -nm 'Initialized DVC'")


def initialize_dvc_storage(dvc_remote_name: str, dvc_remote_url: str) -> None:
    if not run_shell_command("dvc remote list"):
        DATA_UTILS_LOGGER.info("Initializing DVC storage")
        run_shell_command(f"dvc remote add -d {dvc_remote_name} {dvc_remote_url}")
        run_shell_command("git add .dvc/config")
        run_shell_command(f"git commit -nm 'Configure remote storage at: {dvc_remote_url}'")
    else:
        DATA_UTILS_LOGGER.info("DVC storage was already initialized...")


def commit_to_dvc(dvc_raw_data_folder: str, dvc_remote_name: str):
    DATA_UTILS_LOGGER.info("Committing to DVC")

    try:
        # Fetch the current version
        current_version = run_shell_command("git tag --list | sort -t v -k 2 -g | tail -1 | sed 's/v//'").strip()

        # Default to '0' if no version is found
        current_version = current_version or "0"
        next_version = f"v{int(current_version)+1}"

        # Add data to DVC
        run_shell_command(f"dvc add {dvc_raw_data_folder}")
        print("oi")
        # Stage changes
        run_shell_command("git add .")

        # Check Git status to ensure there are changes to commit
        # git_status = check_output(["git", "status", "--porcelain"]).decode().strip()
        # if not git_status:
        #     DATA_UTILS_LOGGER.info("No changes to commit.")
        #     return

        # Commit changes
        run_shell_command(f"git commit -nm 'Updated version of the data from v{current_version} to {next_version}'")

        # Tag the commit
        run_shell_command(f"git tag -a {next_version} -m 'Data version {next_version}'")

        # Push changes
        run_shell_command(f"dvc push {dvc_raw_data_folder}.dvc --remote {dvc_remote_name}")
        run_shell_command("git push --follow-tags")
        run_shell_command("git push -f --tags")

    except CalledProcessError as e:
        DATA_UTILS_LOGGER.error(f"Command failed: {e.cmd}\nReturn code: {e.returncode}\nOutput: {e.output}")
        raise
    except SubprocessError as e:
        DATA_UTILS_LOGGER.error(f"Subprocess error occurred: {str(e)}")
        raise
    except Exception as e:
        DATA_UTILS_LOGGER.error(f"Unexpected error occurred: {str(e)}")
        raise

    finally:
        # Ensure the DVC push is executed even if the commit process fails
        run_shell_command(f"dvc add {dvc_raw_data_folder}")
        run_shell_command(f"dvc push -r {dvc_remote_name}")


def make_new_data_version(dvc_raw_data_folder: str, dvc_remote_name: str) -> None:
    try:
        status = run_shell_command(f"dvc status {dvc_raw_data_folder}.dvc")
        if status == "Data and pipelines are up to date.\n":
            DATA_UTILS_LOGGER.info("Data and pipelines are up to date.")
            return
        commit_to_dvc(dvc_raw_data_folder, dvc_remote_name)
    except CalledProcessError:
        commit_to_dvc(dvc_raw_data_folder, dvc_remote_name)
