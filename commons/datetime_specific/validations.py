# validations.py
'''
This module contains various methods to perform validations on the datetime.
'''

from datetime import datetime
import logging
from commons.structured_responses import validation_conversion_method_responses as valconresponse

logger = logging.getLogger(__name__)


def validate_conformance_to_datetime_format(datetime_str, strptime_format):
    '''
    This method returns back the datetime converted object from the string received.
    Author: Ankur Saxena

    Input:
        datetime_str : the string value of the datetime
        strptime_format : the format that the string is formatted in string so as to create the corresponding datetime object.
                        e.g. %Y-%m-%d
                        (different formats can be seen here:
                        https://www.programiz.com/python-programming/datetime/strptime
                        https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
                        )
    '''
    # Creating a response object.
    resp_obj = valconresponse.ValConResponseDict()

    # Here, we will put in the try block and see that there should not be any error in the converting the datetime.
    flg_error = False
    try:
        datetime_obj = datetime.strptime(datetime_str, strptime_format)
        resp_obj.consolidate_method_for_resp_obj_population(execution_status=1, execution_status_comments='Executed Successfully'
                                                            , execution_detail_section={}
                                                            , objective_status=1, objective_status_comments='Executed Successfully'
                                                            , objective_value= datetime_obj)

    except Exception as error:
        print(error)
        logger.debug(f' while converting the string {datetime_str} to datetime object via the format {strptime_format}'
                     , exc_info=True)
        flg_error = True

    if flg_error:
        resp_obj.consolidate_method_for_resp_obj_population(execution_status=1,
                                                            execution_status_comments='Executed Successfully'
                                                            , execution_detail_section={}
                                                            # Here, the objective status was to get the datetime object but it is not sufficed
                                                            # due to conversion error.
                                                            # here value is not gathered. and error might have come, gather the stack trace and set the error.
                                                            # Probably, let's keep the consolidated error and not the stack trace here; error can be captured somewhere in the logs or  DB.
                                                            , objective_status=0, objective_status_comments=error
                                                            , objective_value='')


# For testing.