import os
from importlib.metadata import version

from toolviper.utils.logger import setup_logger

from . import calibration
from . import utilities

__version__ = version("ohisama")

# Setup default logger instance for module
if not os.getenv("VIPER_LOGGER_NAME"):
    os.environ["VIPER_LOGGER_NAME"] = "ohisama"
    setup_logger(
        logger_name="ohisama",
        log_to_term=True,
        log_to_file=False,
        log_file="ohisama-logfile",
        log_level="INFO",
    )