import warnings # pragma: no cover
class UnknownError(Exception): pass # pragma: no cover
def exception_type_from_error_code(error_code): return dict() # pragma: no cover
def SomeError(node_def, op, message): return 'Some error occurred' # pragma: no cover
error_code = 999 # pragma: no cover
node_def = 'node' # pragma: no cover
op = 'operation' # pragma: no cover
message = 'An error happened' # pragma: no cover

def exception_type_from_error_code(error_code): return {999: SomeError} # pragma: no cover
error_code = 999 # pragma: no cover
node_def = 'node_def' # pragma: no cover
op = 'operation' # pragma: no cover
message = 'Some error message' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
from l3.Runtime import _l_
try:
    _l_(9685)

    exc_type = exception_type_from_error_code(error_code)
    _l_(9680)
    aux = exc_type(node_def, op, message)
    _l_(9681)
    exit(aux)
except KeyError:
    _l_(9684)

    warnings.warn("Unknown error code: %d" % error_code)
    _l_(9682)
    aux = UnknownError(node_def, op, message, error_code)
    _l_(9683)
    exit(aux)
