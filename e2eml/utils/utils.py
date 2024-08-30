import logging
import socket
import subprocess


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(f"[{socket.gethostname()}] {name}")


def run_shell_command(cmd: str) -> str:
    print("test")
    try:
        result = subprocess.run(cmd, text=True, shell=True, check=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Command '{cmd}' failed with return code {e.returncode}")
        print(f"Error output: {e.stderr}")
        raise
