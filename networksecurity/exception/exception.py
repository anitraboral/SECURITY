import sys
from networksecurity.logger.logger import logger


class NetworkSecurityException(Exception):
    def __init__(self, message, error_details: sys):
        super().__init__(message)

        self.error_message = message

        _, _, exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return (
            f"Error occurred in Python script: [{self.file_name}] "
            f"at line number: [{self.lineno}] "
            f"error message: [{self.error_message}]"
        )


if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logger.exception("An exception occurred")
        raise NetworkSecurityException(e, sys) from e