from src.common.custom_logger import CustomLogger
from src.common.exceptions import CustomException

if __name__ == "__main__":
    logger = CustomLogger()
    logger.log_info("Starting model build")

    try:
        4 / 0
    except ZeroDivisionError as ze:
        error_message = "Encountered a division by zero error."
        exc_tb = ze.__traceback__
        # custom_exception = CustomException(exc_tb, error_message)
        # logger.log_error(custom_exception
        # raise ze
        raise CustomException("This is a custom error message") from ze

    except Exception as e:
        # For other exceptions
        exc_tb = e.__traceback__
        custom_exception = CustomException(exc_tb)
        logger.log_error(custom_exception)
