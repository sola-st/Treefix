def exception_type_from_error_code(error_code): return ValueError # pragma: no cover
error_code = 404 # pragma: no cover
node_def = 'node_definition' # pragma: no cover
op = 'operation' # pragma: no cover
message = 'An error occurred' # pragma: no cover
class UnknownError(Exception):# pragma: no cover
    def __init__(self, node_def, op, message, error_code):# pragma: no cover
        super().__init__(f'{node_def}, {op}, {message}, {error_code}') # pragma: no cover
warnings = type('Mock', (object,), {'warn': lambda msg: print(f'Warning: {msg}')}) # pragma: no cover

import warnings # pragma: no cover
import sys # pragma: no cover

def exception_type_from_error_code(error_code): # pragma: no cover
    class CustomException(Exception): # pragma: no cover
        def __init__(self, node_def, op, message): # pragma: no cover
            super().__init__(message) # pragma: no cover
            self.node_def = node_def # pragma: no cover
            self.op = op # pragma: no cover
    return CustomException # pragma: no cover
error_code = 1 # pragma: no cover
node_def = 'node_definition' # pragma: no cover
op = 'operation' # pragma: no cover
message = 'An error occurred' # pragma: no cover
class UnknownError(Exception): # pragma: no cover
    def __init__(self, node_def, op, message, error_code): # pragma: no cover
        super().__init__(f'UnknownError: {message}, Node: {node_def}, Operation: {op}, Error code: {error_code}') # pragma: no cover
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
