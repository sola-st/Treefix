import traceback # pragma: no cover
import requests # pragma: no cover
import json # pragma: no cover
import logging # pragma: no cover

utilities = type('Mock', (object,), {'requests_call': lambda verb, url, **kwargs: (type('MockResponse', (object,), {'json': lambda: {}, 'status_code': 200})(), None), 'process_json_requests_call': lambda verb, url, **kwargs: (True, type('MockResponse', (object,), {'json': lambda: {'_source': {'status_text': 'successfully completed'}}, 'status_code': 200})())})() # pragma: no cover
search_string = 'test_search_string' # pragma: no cover
MainWindow = type('MockMainWindow', (object,), {'the': classmethod(lambda cls: type('Mock', (object,), {'visual_log': lambda msg, log_level=None: print(msg)})())}) # pragma: no cover
logging = type('MockLogging', (object,), {'ERROR': 'ERROR'}) # pragma: no cover
json = type('MockJSON', (object,), {'dumps': json.dumps}) # pragma: no cover
logger = type('MockLogger', (object,), {'error': lambda msg: print(msg)})() # pragma: no cover
ES_URL = 'http://localhost:9200/' # pragma: no cover
INDEX_NAME = 'my_index' # pragma: no cover
traceback = type('MockTraceback', (object,), {'extract_stack': lambda: ['stack_frame_1', 'stack_frame_2'], 'format_list': lambda raw_tb: raw_tb}) # pragma: no cover
requests = type('MockRequests', (object,), {'request': lambda verb, url, **kwargs: type('MockResponse', (object,), {'json': lambda: {}, 'status_code': 200})(), 'Timeout': type('MockTimeout', (BaseException,), {})}) # pragma: no cover

import requests # pragma: no cover
import json # pragma: no cover
import logging # pragma: no cover
import traceback # pragma: no cover

search_string = 'test_search' # pragma: no cover
MainWindow = type('Mock', (object,), {'the': staticmethod(lambda: type('Mock', (object,), {'visual_log': lambda msg, log_level: None})())})() # pragma: no cover
logger = type('Mock', (object,), {'error': lambda msg: print(f'ERROR: {msg}')})() # pragma: no cover
ES_URL = 'http://localhost:9200/' # pragma: no cover
INDEX_NAME = 'test_index' # pragma: no cover
traceback = traceback # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
# see the docs: if you set no timeout the call never times out! A tuple means "max 
# connect time" and "max read time"
from l3.Runtime import _l_
DEFAULT_REQUESTS_TIMEOUT = (5, 15) # for example
_l_(13043) # for example

def log_exception(e, verb, url, kwargs):
    _l_(13049)

    # the reason for making this a separate function will become apparent
    raw_tb = traceback.extract_stack()
    _l_(13044)
    if 'data' in kwargs and len(kwargs['data']) > 500:
        _l_(13046)

        kwargs['data'] = f'{kwargs["data"][:500]}...'  
        _l_(13045)  
    msg = f'BaseException raised: {e.__class__.__module__}.{e.__class__.__qualname__}: {e}\n' \
        + f'verb {verb}, url {url}, kwargs {kwargs}\n\n' \
        + 'Stack trace:\n' + ''.join(traceback.format_list(raw_tb[:-2]))
    _l_(13047)
    logger.error(msg) 
    _l_(13048) 

def requests_call(verb, url, **kwargs):
    _l_(13060)

    response = None
    _l_(13050)
    exception = None
    _l_(13051)
    try:
        _l_(13058)

        if 'timeout' not in kwargs:
            _l_(13053)

            kwargs['timeout'] = DEFAULT_REQUESTS_TIMEOUT
            _l_(13052)
        response = requests.request(verb, url, **kwargs)
        _l_(13054)
    except BaseException as e:
        _l_(13057)

        log_exception(e, verb, url, kwargs)
        _l_(13055)
        exception = e
        _l_(13056)
    aux = (response, exception)
    _l_(13059)
    return aux

search_response, exception = utilities.requests_call('get',
    f'http://localhost:9200/my_index/_search?q={search_string}')
_l_(13061)

if search_response == None:
    _l_(13065)

    # you might check here for (e.g.) a requests.Timeout, tailoring the message
    # accordingly, as the kind of error anyone might be expected to understand
    msg = f'No response searching on |{search_string}|. See log'
    _l_(13062)
    MainWindow.the().visual_log(msg, log_level=logging.ERROR)
    _l_(13063)
    aux = ""
    _l_(13064)
    return aux
response_json = search_response.json()
_l_(13066)
if search_response.status_code != 200:
    _l_(13072)

    msg = f'Bad response searching on |{search_string}|. See log'
    _l_(13067)
    MainWindow.the().visual_log(msg, log_level=logging.ERROR)
    _l_(13068)
    # usually response_json will give full details about the problem
    log_msg = f'search on |{search_string}| bad response\n{json.dumps(response_json, indent=4)}'
    _l_(13069)
    logger.error(log_msg)
    _l_(13070)
    aux = ""
    _l_(13071)
    return aux

# now examine the keys and values in response_json: these may of course 
# indicate an error of some kind even though the response returned OK (status 200)... 

def log_response_error(response_type, call_name, deliverable, verb, url, **kwargs):
    _l_(13090)

    # NB this function can also be used independently
    if response_type == 'No':
        _l_(13088)

        if isinstance(deliverable, requests.Timeout):
            _l_(13075)

            MainWindow.the().visual_log(f'Time out of {call_name} before response received!', logging.ERROR)
            _l_(13073)
            aux = ""    
            _l_(13074)    
            return aux    
    else:
        if isinstance(deliverable, BaseException):
            _l_(13087)

            # NB if response.json() raises an exception we end up here
            log_exception(deliverable, verb, url, kwargs)
            _l_(13076)
        else:
            # if we get here no exception has been raised, so no stack trace has yet been logged.  
            # a response has been returned, but is either "Bad" or "Anomalous"
            response_json = deliverable.json()
            _l_(13077)

            raw_tb = traceback.extract_stack()
            _l_(13078)
            if 'data' in kwargs and len(kwargs['data']) > 500:
                _l_(13080)

                kwargs['data'] = f'{kwargs["data"][:500]}...'
                _l_(13079)
            added_message = ''     
            _l_(13081)     
            if hasattr(deliverable, 'added_message'):
                _l_(13084)

                added_message = deliverable.added_message + '\n'
                _l_(13082)
                del deliverable.added_message
                _l_(13083)
            call_and_response_details = f'{response_type} response\n{added_message}' \
                + f'verb {verb}, url {url}, kwargs {kwargs}\nresponse:\n{json.dumps(response_json, indent=4)}'
            _l_(13085)
            logger.error(f'{call_and_response_details}\nStack trace: {"".join(traceback.format_list(raw_tb[:-1]))}')
            _l_(13086)
    MainWindow.the().visual_log(f'{response_type} response {call_name}. See log.', logging.ERROR)
    _l_(13089)
def check_keys(req_dict_structure, response_dict_structure, response):
    _l_(13128)

    # so this function is about checking the keys in the returned json object...
    # NB both structures MUST be dicts
    if not isinstance(req_dict_structure, dict):
        _l_(13093)

        response.added_message = f'req_dict_structure not dict: {type(req_dict_structure)}\n'
        _l_(13091)
        aux = False
        _l_(13092)
        return aux
    if not isinstance(response_dict_structure, dict):
        _l_(13096)

        response.added_message = f'response_dict_structure not dict: {type(response_dict_structure)}\n'
        _l_(13094)
        aux = False
        _l_(13095)
        return aux
    for dict_key in req_dict_structure.keys():
        _l_(13126)

        if dict_key not in response_dict_structure:
            _l_(13099)

            response.added_message = f'key |{dict_key}| missing\n'
            _l_(13097)
            aux = False
            _l_(13098)
            return aux
        req_value = req_dict_structure[dict_key]
        _l_(13100)
        response_value = response_dict_structure[dict_key]
        _l_(13101)
        if isinstance(req_value, dict):
            _l_(13125)

            # if the response at this point is a list apply the req_value dict to each element:
            # failure in just one such element leads to "Anomalous response"... 
            if isinstance(response_value, list):
                _l_(13107)

                for resp_list_element in response_value:
                    _l_(13104)

                    if not check_keys(req_value, resp_list_element, response):
                        _l_(13103)

                        aux = False
                        _l_(13102)
                        return aux
            elif not check_keys(req_value, response_value, response):
                _l_(13106)

                aux = False
                _l_(13105)
                return aux
        elif isinstance(req_value, list):
            _l_(13124)

            if not isinstance(response_value, list):
                _l_(13110)

                response.added_message = f'key |{dict_key}| not list: {type(response_value)}\n'
                _l_(13108)
                aux = False
                _l_(13109)
                return aux
            # it is OK for the value to be a list, but these must be strings (keys) or dicts
            for req_list_element, resp_list_element in zip(req_value, response_value):
                _l_(13120)

                if isinstance(req_list_element, dict):
                    _l_(13113)

                    if not check_keys(req_list_element, resp_list_element, response):
                        _l_(13112)

                        aux = False
                        _l_(13111)
                        return aux
                if not isinstance(req_list_element, str):
                    _l_(13116)

                    response.added_message = f'req_list_element not string: {type(req_list_element)}\n'
                    _l_(13114)
                    aux = False
                    _l_(13115)
                    return aux
                if req_list_element not in response_value:
                    _l_(13119)

                    response.added_message = f'key |{req_list_element}| missing from response list\n'
                    _l_(13117)
                    aux = False
                    _l_(13118)
                    return aux
        # put None as a dummy value (otherwise something like {'my_key'} will be seen as a set, not a dict 
        elif req_value != None:
            _l_(13123)

            response.added_message = f'required value of key |{dict_key}| must be None (dummy), dict or list: {type(req_value)}\n'
            _l_(13121)
            aux = False
            _l_(13122)
            return aux
    aux = True
    _l_(13127)
    return aux

def process_json_requests_call(verb, url, **kwargs):
    _l_(13164)

    # "call_name" is a mandatory kwarg
    if 'call_name' not in kwargs:
        _l_(13130)

        raise Exception('kwarg "call_name" not supplied!')
        _l_(13129)
    call_name = kwargs['call_name']
    _l_(13131)
    del kwargs['call_name']
    _l_(13132)

    required_keys = {}    
    _l_(13133)    
    if 'required_keys' in kwargs:
        _l_(13136)

        required_keys = kwargs['required_keys']
        _l_(13134)
        del kwargs['required_keys']
        _l_(13135)

    acceptable_statuses = [200]
    _l_(13137)
    if 'acceptable_statuses' in kwargs:
        _l_(13140)

        acceptable_statuses = kwargs['acceptable_statuses']
        _l_(13138)
        del kwargs['acceptable_statuses']
        _l_(13139)

    exception_handler = log_response_error
    _l_(13141)
    if 'exception_handler' in kwargs:
        _l_(13144)

        exception_handler = kwargs['exception_handler']
        _l_(13142)
        del kwargs['exception_handler']
        _l_(13143)
    response, exception = requests_call(verb, url, **kwargs)
    _l_(13145)

    if response == None:
        _l_(13148)

        exception_handler('No', call_name, exception, verb, url, **kwargs)
        _l_(13146)
        aux = (False, exception)
        _l_(13147)
        return aux
    try:
        _l_(13154)

        response_json = response.json()
        _l_(13149)
    except BaseException as e:
        _l_(13153)

        logger.error(f'response.status_code {response.status_code} but calling json() raised exception')
        _l_(13150)
        # an exception raised at this point can't truthfully lead to a "No response" message... so say "bad"
        exception_handler('Bad', call_name, e, verb, url, **kwargs)
        _l_(13151)
        aux = (False, response)
        _l_(13152)
        return aux
    status_ok = response.status_code in acceptable_statuses
    _l_(13155)
    if not status_ok:
        _l_(13159)

        response.added_message = f'status code was {response.status_code}'
        _l_(13156)
        log_response_error('Bad', call_name, response, verb, url, **kwargs)
        _l_(13157)
        aux = (False, response)
        _l_(13158)
        return aux
    check_result = check_keys(required_keys, response_json, response)
    _l_(13160)
    if not check_result:
        _l_(13162)

        log_response_error('Anomalous', call_name, response, verb, url, **kwargs)
        _l_(13161)
    aux = (check_result, response)      
    _l_(13163)      
    return aux      

success, deliverable = utilities.process_json_requests_call('get', 
    f'{ES_URL}{INDEX_NAME}/_doc/1', 
    call_name=f'checking index {INDEX_NAME}',
    required_keys={'_source':{'status_text': None}})
_l_(13165)
if not success:
    _l_(13166)

return False# here, we know the deliverable is a response, not an exception
# we also don't need to check for the keys being present: 
# the generic code has checked that all expected keys are present
index_status = deliverable.json()['_source']['status_text']
_l_(13167)
if index_status != 'successfully completed':
    _l_(13172)

    # ... i.e. an example of a 200 response, but an error nonetheless
    msg = f'Error response: ES index {INDEX_NAME} does not seem to have been built OK: cannot search'
    _l_(13168)
    MainWindow.the().visual_log(msg)
    _l_(13169)
    logger.error(f'index |{INDEX_NAME}|: deliverable.json() {json.dumps(deliverable.json(), indent=4)}')
    _l_(13170)
    aux = False
    _l_(13171)
    return aux

