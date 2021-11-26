# validation_conversion_method_responses.py
'''
This file contains the structure as to how the methods that does some kind of
validation and/or conversion would return the output in the form of.
'''


class ExecutionResponseDict:
    ''' Method to formulate the response of an execution method '''
    # {'STATUS': 'SUCCESS',
    # 'STATUS_COMMENTS': 'executed_successfully',
    # 'DETAIL_SECTION': {
    #     'DATABASE_NAME': {'value': 'PHILIPS_BCM', 'comment': 'This is the Mongo DB connected for this stage'},
    #     'FUNCTION_COLLECTION': {'value': 'TFA02_COPY',
    #                             'comment': 'This is the Mongo DB collection operated upon for this stage'},
    #     'RUN_ID': {'value': '1b90f9d5-094d-4816-a8a8-8ddf04247486-1622726323002',
    #                'comment': 'This is the runID passed for this stage execution'},
    #     'RESULT_FROM_OPERATION': {'value': 'UPDATE_MANY', 'comment': 'modified count = 0 matched count =  0 '}}}

    def __init__(self):
       self.method_op_dict = {'STATUS': '', 'STATUS_COMMENTS': '', 'DETAIL_SECTION': {}}

    def add_to_detail_section_dict(self, keyname, value, comment):
        ''' Method to add to the detail section of the response to be passed from the stage to the pipeline'''
        self.method_op_dict['DETAIL_SECTION'][keyname] = {'value': value, 'comment': comment}

    def add_to_status(self, status):
        ''' set to SUCCESS if 1 is passed else Failure for all other values'''
        # self.method_op_dict['STATUS'] = 'SUCCESS' if status == 1 else 'FAILURE'
        if status == 1:
            self.method_op_dict['STATUS'] = 'SUCCESS'
        elif status == 0:
            self.method_op_dict['STATUS'] = 'FAILURE'
        else:
            self.method_op_dict['STATUS'] = status      # for eg yesID, noID passed for decision type of nodes.

    def add_to_status_comments(self, status_comments):
        self.method_op_dict['STATUS_COMMENTS'] = status_comments


class ValConResponseDict(ExecutionResponseDict):

    '''
    Author : Ankur Saxena

    Objective : The instance of this class will return the structured response conforming to the structure as prescribed
                by this class. This response can be used by the Called methods to return to the Caller methods.
                Majorly these can be used by the methods that does some kind of validation and/or conversion.

                This has 2 parts:
                1. an Execution Status object: That defines the details around the execution of the method.
                  This it inherits from the ExecutionResponseDict class.
                2. Objective Status : That defines whether the objective was realized and what is the value.

                An example, the method to convert the string to datetime with the given format;
                So, if the execution status is True i.e. it executed fine, but could be that the string was not in a
                proper format to be converted and hence the objective status that the string be returned as an datetime
                object has failed.
                So, in this case EXECUTION_STATUS : True; OBJECTIVE_STATUS : False.
                If the objective returned the value fine then :
                OBJECTIVE_STATUS : True
                OBJECTIVE_VALUE : datetime converted value.
                OBJECTIVE_TYPE : datetime ; whatever we gathered from the type() in this case <class 'datetime.datetime'>

    The o/p format look like as below:
    {'STATUS': 'SUCCESS',
     'STATUS_COMMENTS': 'executed_successfully',
     'DETAIL_SECTION': {
         'DATABASE_NAME': {'value': 'PHILIPS_BCM', 'comment': 'This is the Mongo DB connected for this stage'},
         'FUNCTION_COLLECTION': {'value': 'TFA02_COPY',
                                 'comment': 'This is the Mongo DB collection operated upon for this stage'},
         'RUN_ID': {'value': '1b90f9d5-094d-4816-a8a8-8ddf04247486-1622726323002',
                    'comment': 'This is the runID passed for this stage execution'},
         'RESULT_FROM_OPERATION': {'value': 'UPDATE_MANY', 'comment': 'modified count = 0 matched count =  0 '}
            }
     'OBJECTIVE' :
        {'STATUS': 'SUCCESS'
        ,'VALUE': The datetime object will be here.
        ,'TYPE': <class 'datetime.datetime'>
        ,'STATUS_COMMENTS': 'Executed Successfully'
        }
    }
    '''

    # Here , since the __init__ method in the base class that is ExecutionResponseDict is creating the needed dictionary
    # for the output response , here there is no need to override the __init__ method and hence not defining the
    # __init__ method for the child class here.

    # on another view , we need to add the OBJECTIVE dictionary to the output response.
    def __init__(self):
        # this will override the method of the base class , so as we want that functionality to also happen
        # hence we will call the base class init method.
        super().__init__()  # this will populate the attribute method_op_dict

        # Now, we need to add the OBJECTIVE section to the output response dict as well.
        self.method_op_dict['OBJECTIVE'] = dict()
        self.method_op_dict['OBJECTIVE']['STATUS'] = ''
        self.method_op_dict['OBJECTIVE']['VALUE'] = ''
        self.method_op_dict['OBJECTIVE']['TYPE'] = ''
        self.method_op_dict['OBJECTIVE']['STATUS_COMMENTS'] = ''

    # However, we will define couple of methods to populate

    def add_to_obj_section_status(self, status):
        ''' set to SUCCESS if 1 is passed else Failure for all other values'''
        if status == 1:
            self.method_op_dict['OBJECTIVE']['STATUS'] = 'SUCCESS'
        elif status == 0:
            self.method_op_dict['OBJECTIVE']['STATUS'] = 'FAILURE'
        else:
            # Any other value if it gets recognized later upon.
            self.method_op_dict['OBJECTIVE']['STATUS'] = status

    def add_to_obj_section_status_comments(self, status_comments):
        self.method_op_dict['OBJECTIVE']['STATUS_COMMENTS'] = status_comments

    def add_to_obj_section_value_and_type(self, value):
        # This value can be a dictionary again or a particular value of a specific type example datetime object.
        self.method_op_dict['OBJECTIVE']['VALUE'] = value
        self.method_op_dict['OBJECTIVE']['TYPE'] = type(value)

    def consolidate_method_for_resp_obj_population(self
                                                   , execution_status='', execution_status_comments=''
                                                   , execution_detail_section={}
                                                   , objective_status='', objective_status_comments=''
                                                   , objective_value=''):
        '''
        This method gives one touchpoint update for the entire object population.
        All the values are important to be provided; else the default values above will be filled in,
        as we can see the status values would also be populated with blanks if not provided.
        So the dict that need to be passed to this consolidate method to follow the form as :
        {KEYNAME : {'value':value, 'comment':commentss} }
        '''

        self.add_to_status(execution_status)
        self.add_to_status_comments(execution_status_comments)
        self.add_to_obj_section_status(objective_status)
        self.add_to_obj_section_status_comments(objective_status_comments)
        self.add_to_obj_section_value_and_type(objective_value)

        # Now , for populating the execution detail section which has a dictionary like as follows:
        # 'DETAIL_SECTION': \
        #     {
        #     'DATABASE_NAME': {'value': 'PHILIPS_BCM', 'comment': 'This is the Mongo DB connected for this stage'},
        #     'FUNCTION_COLLECTION': {'value': 'TFA02_COPY',
        #                             'comment': 'This is the Mongo DB collection operated upon for this stage'},
        #     'RUN_ID': {'value': '1b90f9d5-094d-4816-a8a8-8ddf04247486-1622726323002',
        #                'comment': 'This is the runID passed for this stage execution'},
        #     'RESULT_FROM_OPERATION': {'value': 'UPDATE_MANY', 'comment': 'modified count = 0 matched count =  0 '}
        #     }
        # i.e. of the form as {'keyname': {'value': value, 'comment':comment}}

        for dict_key, dict_val in execution_detail_section.items():
            # For {'keyname1':{'value':1,'comment':'ccc1'}, 'keyname2':{'value':2,'comment':'ccc2'}}
            # dict_key will be keyname1, keyname2 and dict_val will be {'value':1,'comment':'ccc1'}, {'value':2,'comment':'ccc2'}
            # for each of the keyname , value, comment we need to call this method.
            keyname = dict_key
            # Here, we are checking if the dict_val is not a dictionary which is needed for this response output.
            # even if its not passed as that it should work.
            if isinstance(dict_val, dict):

                value = dict_val.get('value', '')
                comment = dict_val.get('comment', '')

            else:

                value = dict_val
                comment = ''

            # recursively called.
            self.add_to_detail_section_dict(keyname, value, comment)
