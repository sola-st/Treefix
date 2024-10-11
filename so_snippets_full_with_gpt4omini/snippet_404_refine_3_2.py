import requests # pragma: no cover
import json # pragma: no cover
import logging # pragma: no cover
import traceback # pragma: no cover

class MockLogger:# pragma: no cover
    def error(self, msg): pass# pragma: no cover
logger = MockLogger() # pragma: no cover
class MockMainWindow:# pragma: no cover
    @staticmethod# pragma: no cover
    def the():# pragma: no cover
        return MockMainWindow()# pragma: no cover
    def visual_log(self, msg, log_level): pass# pragma: no cover
MainWindow = MockMainWindow # pragma: no cover
utilities = type('MockUtilities', (object,), {'requests_call': lambda verb, url, **kwargs: (None, requests.Timeout()), 'process_json_requests_call': lambda verb, url, **kwargs: (False, None)})() # pragma: no cover
search_string = 'test_query' # pragma: no cover
ES_URL = 'http://localhost:9200/' # pragma: no cover
INDEX_NAME = 'my_index' # pragma: no cover

import requests # pragma: no cover
import json # pragma: no cover
import logging # pragma: no cover
import traceback # pragma: no cover

class MockLogger:# pragma: no cover
    def error(self, msg): print(f'ERROR: {msg}')# pragma: no cover
logger = MockLogger() # pragma: no cover
class MockMainWindow:# pragma: no cover
    @staticmethod# pragma: no cover
    def the():# pragma: no cover
        return MockMainWindow()# pragma: no cover
    def visual_log(self, msg, log_level): print(f'{log_level}: {msg}')# pragma: no cover
MainWindow = MockMainWindow # pragma: no cover
utilities = type('MockUtilities', (object,), {'requests_call': lambda verb, url, **kwargs: (MockResponse(), None), 'process_json_requests_call': lambda verb, url, **kwargs: (True, MockResponse())})() # pragma: no cover
class MockResponse:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.status_code = 200# pragma: no cover
        self._json = {'_source': {'status_text': 'successfully completed'}}# pragma: no cover
    def json(self): return self._json # pragma: no cover
search_string = 'test_query' # pragma: no cover
ES_URL = 'http://localhost:9200/' # pragma: no cover
INDEX_NAME = 'my_index' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
# see the docs: if you set no timeout the call never times out! A tuple means "max 
# connect time" and "max read time"
from l3.Runtime import _l_
DEFAULT_REQUESTS_TIMEOUT = (5, 15) # for example
_l_(691) # for example

def log_exception(e, verb, url, kwargs):
    _l_(697)

    # the reason for making this a separate function will become apparent
    raw_tb = traceback.extract_stack()
    _l_(692)
    if 'data' in kwargs and len(kwargs['data']) > 500:
        _l_(694)

        kwargs['data'] = f'{kwargs["data"][:500]}...'  
        _l_(693)  
    msg = f'BaseException raised: {e.__class__.__module__}.{e.__class__.__qualname__}: {e}\n' \
        + f'verb {verb}, url {url}, kwargs {kwargs}\n\n' \
        + 'Stack trace:\n' + ''.join(traceback.format_list(raw_tb[:-2]))
    _l_(695)
    logger.error(msg) 
    _l_(696) 

def requests_call(verb, url, **kwargs):
    _l_(708)

    response = None
    _l_(698)
    exception = None
    _l_(699)
    try:
        _l_(706)

        if 'timeout' not in kwargs:
            _l_(701)

            kwargs['timeout'] = DEFAULT_REQUESTS_TIMEOUT
            _l_(700)
        response = requests.request(verb, url, **kwargs)
        _l_(702)
    except BaseException as e:
        _l_(705)

        log_exception(e, verb, url, kwargs)
        _l_(703)
        exception = e
        _l_(704)
    aux = (response, exception)
    _l_(707)
    return aux

search_response, exception = utilities.requests_call('get',
    f'http://localhost:9200/my_index/_search?q={search_string}')
_l_(709)

if search_response == None:
    _l_(713)

    # you might check here for (e.g.) a requests.Timeout, tailoring the message
    # accordingly, as the kind of error anyone might be expected to understand
    msg = f'No response searching on |{search_string}|. See log'
    _l_(710)
    MainWindow.the().visual_log(msg, log_level=logging.ERROR)
    _l_(711)
    aux = ""
    _l_(712)
    return aux
response_json = search_response.json()
_l_(714)
if search_response.status_code != 200:
    _l_(720)

    msg = f'Bad response searching on |{search_string}|. See log'
    _l_(715)
    MainWindow.the().visual_log(msg, log_level=logging.ERROR)
    _l_(716)
    # usually response_json will give full details about the problem
    log_msg = f'search on |{search_string}| bad response\n{json.dumps(response_json, indent=4)}'
    _l_(717)
    logger.error(log_msg)
    _l_(718)
    aux = ""
    _l_(719)
    return aux

# now examine the keys and values in response_json: these may of course 
# indicate an error of some kind even though the response returned OK (status 200)... 

def log_response_error(response_type, call_name, deliverable, verb, url, **kwargs):
    _l_(738)

    # NB this function can also be used independently
    if response_type == 'No':
        _l_(736)

        if isinstance(deliverable, requests.Timeout):
            _l_(723)

            MainWindow.the().visual_log(f'Time out of {call_name} before response received!', logging.ERROR)
            _l_(721)
            aux = ""    
            _l_(722)    
            return aux    
    else:
        if isinstance(deliverable, BaseException):
            _l_(735)

            # NB if response.json() raises an exception we end up here
            log_exception(deliverable, verb, url, kwargs)
            _l_(724)
        else:
            # if we get here no exception has been raised, so no stack trace has yet been logged.  
            # a response has been returned, but is either "Bad" or "Anomalous"
            response_json = deliverable.json()
            _l_(725)

            raw_tb = traceback.extract_stack()
            _l_(726)
            if 'data' in kwargs and len(kwargs['data']) > 500:
                _l_(728)

                kwargs['data'] = f'{kwargs["data"][:500]}...'
                _l_(727)
            added_message = ''     
            _l_(729)     
            if hasattr(deliverable, 'added_message'):
                _l_(732)

                added_message = deliverable.added_message + '\n'
                _l_(730)
                del deliverable.added_message
                _l_(731)
            call_and_response_details = f'{response_type} response\n{added_message}' \
                + f'verb {verb}, url {url}, kwargs {kwargs}\nresponse:\n{json.dumps(response_json, indent=4)}'
            _l_(733)
            logger.error(f'{call_and_response_details}\nStack trace: {"".join(traceback.format_list(raw_tb[:-1]))}')
            _l_(734)
    MainWindow.the().visual_log(f'{response_type} response {call_name}. See log.', logging.ERROR)
    _l_(737)
def check_keys(req_dict_structure, response_dict_structure, response):
    _l_(776)

    # so this function is about checking the keys in the returned json object...
    # NB both structures MUST be dicts
    if not isinstance(req_dict_structure, dict):
        _l_(741)

        response.added_message = f'req_dict_structure not dict: {type(req_dict_structure)}\n'
        _l_(739)
        aux = False
        _l_(740)
        return aux
    if not isinstance(response_dict_structure, dict):
        _l_(744)

        response.added_message = f'response_dict_structure not dict: {type(response_dict_structure)}\n'
        _l_(742)
        aux = False
        _l_(743)
        return aux
    for dict_key in req_dict_structure.keys():
        _l_(774)

        if dict_key not in response_dict_structure:
            _l_(747)

            response.added_message = f'key |{dict_key}| missing\n'
            _l_(745)
            aux = False
            _l_(746)
            return aux
        req_value = req_dict_structure[dict_key]
        _l_(748)
        response_value = response_dict_structure[dict_key]
        _l_(749)
        if isinstance(req_value, dict):
            _l_(773)

            # if the response at this point is a list apply the req_value dict to each element:
            # failure in just one such element leads to "Anomalous response"... 
            if isinstance(response_value, list):
                _l_(755)

                for resp_list_element in response_value:
                    _l_(752)

                    if not check_keys(req_value, resp_list_element, response):
                        _l_(751)

                        aux = False
                        _l_(750)
                        return aux
            elif not check_keys(req_value, response_value, response):
                _l_(754)

                aux = False
                _l_(753)
                return aux
        elif isinstance(req_value, list):
            _l_(772)

            if not isinstance(response_value, list):
                _l_(758)

                response.added_message = f'key |{dict_key}| not list: {type(response_value)}\n'
                _l_(756)
                aux = False
                _l_(757)
                return aux
            # it is OK for the value to be a list, but these must be strings (keys) or dicts
            for req_list_element, resp_list_element in zip(req_value, response_value):
                _l_(768)

                if isinstance(req_list_element, dict):
                    _l_(761)

                    if not check_keys(req_list_element, resp_list_element, response):
                        _l_(760)

                        aux = False
                        _l_(759)
                        return aux
                if not isinstance(req_list_element, str):
                    _l_(764)

                    response.added_message = f'req_list_element not string: {type(req_list_element)}\n'
                    _l_(762)
                    aux = False
                    _l_(763)
                    return aux
                if req_list_element not in response_value:
                    _l_(767)

                    response.added_message = f'key |{req_list_element}| missing from response list\n'
                    _l_(765)
                    aux = False
                    _l_(766)
                    return aux
        # put None as a dummy value (otherwise something like {'my_key'} will be seen as a set, not a dict 
        elif req_value != None:
            _l_(771)

            response.added_message = f'required value of key |{dict_key}| must be None (dummy), dict or list: {type(req_value)}\n'
            _l_(769)
            aux = False
            _l_(770)
            return aux
    aux = True
    _l_(775)
    return aux

def process_json_requests_call(verb, url, **kwargs):
    _l_(812)

    # "call_name" is a mandatory kwarg
    if 'call_name' not in kwargs:
        _l_(778)

        raise Exception('kwarg "call_name" not supplied!')
        _l_(777)
    call_name = kwargs['call_name']
    _l_(779)
    del kwargs['call_name']
    _l_(780)

    required_keys = {}    
    _l_(781)    
    if 'required_keys' in kwargs:
        _l_(784)

        required_keys = kwargs['required_keys']
        _l_(782)
        del kwargs['required_keys']
        _l_(783)

    acceptable_statuses = [200]
    _l_(785)
    if 'acceptable_statuses' in kwargs:
        _l_(788)

        acceptable_statuses = kwargs['acceptable_statuses']
        _l_(786)
        del kwargs['acceptable_statuses']
        _l_(787)

    exception_handler = log_response_error
    _l_(789)
    if 'exception_handler' in kwargs:
        _l_(792)

        exception_handler = kwargs['exception_handler']
        _l_(790)
        del kwargs['exception_handler']
        _l_(791)
    response, exception = requests_call(verb, url, **kwargs)
    _l_(793)

    if response == None:
        _l_(796)

        exception_handler('No', call_name, exception, verb, url, **kwargs)
        _l_(794)
        aux = (False, exception)
        _l_(795)
        return aux
    try:
        _l_(802)

        response_json = response.json()
        _l_(797)
    except BaseException as e:
        _l_(801)

        logger.error(f'response.status_code {response.status_code} but calling json() raised exception')
        _l_(798)
        # an exception raised at this point can't truthfully lead to a "No response" message... so say "bad"
        exception_handler('Bad', call_name, e, verb, url, **kwargs)
        _l_(799)
        aux = (False, response)
        _l_(800)
        return aux
    status_ok = response.status_code in acceptable_statuses
    _l_(803)
    if not status_ok:
        _l_(807)

        response.added_message = f'status code was {response.status_code}'
        _l_(804)
        log_response_error('Bad', call_name, response, verb, url, **kwargs)
        _l_(805)
        aux = (False, response)
        _l_(806)
        return aux
    check_result = check_keys(required_keys, response_json, response)
    _l_(808)
    if not check_result:
        _l_(810)

        log_response_error('Anomalous', call_name, response, verb, url, **kwargs)
        _l_(809)
    aux = (check_result, response)      
    _l_(811)      
    return aux      

success, deliverable = utilities.process_json_requests_call('get', 
    f'{ES_URL}{INDEX_NAME}/_doc/1', 
    call_name=f'checking index {INDEX_NAME}',
    required_keys={'_source':{'status_text': None}})
_l_(813)
if not success:
    _l_(814)

return False# here, we know the deliverable is a response, not an exception
# we also don't need to check for the keys being present: 
# the generic code has checked that all expected keys are present
index_status = deliverable.json()['_source']['status_text']
_l_(815)
if index_status != 'successfully completed':
    _l_(820)

    # ... i.e. an example of a 200 response, but an error nonetheless
    msg = f'Error response: ES index {INDEX_NAME} does not seem to have been built OK: cannot search'
    _l_(816)
    MainWindow.the().visual_log(msg)
    _l_(817)
    logger.error(f'index |{INDEX_NAME}|: deliverable.json() {json.dumps(deliverable.json(), indent=4)}')
    _l_(818)
    aux = False
    _l_(819)
    return aux

