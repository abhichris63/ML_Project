import sys
import logging


def error_message_detail(error, error_detail:sys):
    """
    This function provides error message and error_details about the error occured.
    """
    # This exc_info() function gives 3 specific information, first 2nd information i am not interested so I will be used the 3rd Information.
    # This exc_info() provides details of the error occured on which file,line,line_number the error as occured.
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in Python script name [{0}], line number [{1}], error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message
