import logging
import os
from enum import Enum

class LoggingType(Enum):
    debug = 1
    info = 2
    warning = 3
    error = 4


class CustomLogger:
    def __init__(self, name: str = "my_project_logger"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        os.makedirs("logs", exist_ok=True)

        if not self.logger.handlers:
            # File handler
            file_handler = logging.FileHandler("logs/app.log")
            file_handler.setLevel(logging.DEBUG)

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            # Formatter
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)


    def write_log(self, msg, level):
        if level == LoggingType.debug:
            self.logger.debug(msg)
        elif level == LoggingType.error:
            self.logger.error(msg)
        elif level == LoggingType.warning:
            self.logger.warning(msg)
        else:
            self.logger.info(msg)


    def get_logger(self):
        """Optional: Access to raw logger if needed."""
        return self.logger
