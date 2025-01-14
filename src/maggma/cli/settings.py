import platform
import tempfile

from pydantic import BaseSettings, Field

tempdir = "/tmp" if platform.system() == "Darwin" else tempfile.gettempdir()


class CLISettings(BaseSettings):
    WORKER_TIMEOUT: int = Field(
        None,
        description="Timeout in seconds for a distributed worker",
    )

    MANAGER_TIMEOUT: int = Field(
        3600,
        description="Timeout in seconds for the worker manager",
    )

    TEMP_DIR: str = Field(
        tempdir,
        description="Directory that memory profile .bin files are dumped to",
    )

    class Config:
        env_prefix = "MAGGMA_"
        extra = "ignore"
