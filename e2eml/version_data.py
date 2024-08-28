from pathlib import Path

from e2eml.config_schemas.config_schema import Config
from e2eml.utils.config_utils import get_config
from e2eml.utils.data_utils import initialize_dvc


@get_config(config_path="../configs", config_name="config")
def version_data(config: Config) -> None:
    initialize_dvc()


if __name__ == "__main__":
    version_data()  # type ignore
