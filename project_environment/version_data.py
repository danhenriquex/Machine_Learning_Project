from pathlib import Path

from project_environment.config_schemas.config_schema import Config
from project_environment.utils.config_utils import get_config
from project_environment.utils.data_utils import get_config, initialize_dvc
from project_environment.utils.utils import get_logger


@get_config(config_path="../configs", config_name="config")
def version_data(config: Config) -> None:
    initialize_dvc()


if __name__ == "__main__":
    version_data()  # type ignore
