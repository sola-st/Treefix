import warnings # pragma: no cover

def exception_type_from_error_code(code): # pragma: no cover
    error_map = {404: FileNotFoundError, 500: RuntimeError, 400: ValueError} # pragma: no cover
    return error_map.get(code, Exception) # pragma: no cover
 # pragma: no cover
error_code = 404 # pragma: no cover
 # pragma: no cover
node_def = {'name': 'node1'} # pragma: no cover
 # pragma: no cover
op = 'operation1' # pragma: no cover
 # pragma: no cover
message = 'An error occurred.' # pragma: no cover
 # pragma: no cover
UnknownError = type('UnknownError', (Exception,), {}) # pragma: no cover
 # pragma: no cover
warnings = type('Mock', (object,), {'warn': lambda self, msg: print(msg)})() # pragma: no cover

import warnings # pragma: no cover

def exception_type_from_error_code(error_code): # pragma: no cover
    class CustomError(Exception): # pragma: no cover
        def __init__(self, node_def, op, message): # pragma: no cover
            super().__init__(f'{message} (Node: {node_def}, Operation: {op})') # pragma: no cover
            self.node_def = node_def # pragma: no cover
            self.op = op # pragma: no cover
            self.message = message # pragma: no cover
    return CustomError # pragma: no cover
 # pragma: no cover
error_code = 1001 # pragma: no cover
 # pragma: no cover
node_def = 'NodeDefinitionExample' # pragma: no cover
 # pragma: no cover
op = 'OperationExample' # pragma: no cover
 # pragma: no cover
message = 'An example error message' # pragma: no cover
 # pragma: no cover
class UnknownError(Exception): # pragma: no cover
    def __init__(self, node_def, op, message, error_code): # pragma: no cover
        super().__init__(f'{message} (Node: {node_def}, Operation: {op}, Error code: {error_code})') # pragma: no cover
        self.node_def = node_def # pragma: no cover
        self.op = op # pragma: no cover
        self.message = message # pragma: no cover
        self.error_code = error_code # pragma: no cover
 # pragma: no cover
warnings = type('Mock', (object,), {'warn': lambda msg: print(f'Warning: {msg}')}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
from l3.Runtime import _l_
try:
    _l_(22047)

    exc_type = exception_type_from_error_code(error_code)
    _l_(22042)
    aux = exc_type(node_def, op, message)
    _l_(22043)
    exit(aux)
except KeyError:
    _l_(22046)

    warnings.warn("Unknown error code: %d" % error_code)
    _l_(22044)
    aux = UnknownError(node_def, op, message, error_code)
    _l_(22045)
    exit(aux)
