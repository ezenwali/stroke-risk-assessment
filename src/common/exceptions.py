"""
Custom Exception Handler
"""


def error_message_detail(error, exc_tb):
    """
    Generate a descriptive error message.
    """
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in Python script '{file_name}' at line number {line_number}: {error}"

    return error_message


class CustomException(Exception):
    """
    Custom Exception class to generate detailed error messages.

    Args:
    - error_message: The error message.
    - exc_tb: Traceback information associated with the error.

    Attributes:
    - error_message (str): A formatted error message including file name, line number, and error description.
    """

    def __init__(self, error_message="Something went wrong", exc_tb=None):
        super().__init__(error_message)
        if exc_tb:
            self.error_message = error_message_detail(error_message, exc_tb)
        else:
            self.error_message = error_message

    def __str__(self):
        return self.error_message
