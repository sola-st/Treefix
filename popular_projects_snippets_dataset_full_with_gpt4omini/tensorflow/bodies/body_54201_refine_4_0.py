def exception_type_from_error_code(error_code): return ValueError # pragma: no cover
error_code = 404 # pragma: no cover
node_def = 'node1' # pragma: no cover
op = 'operation_name' # pragma: no cover
message = 'An error occurred' # pragma: no cover
class UnknownError(Exception): pass # pragma: no cover
warnings = type('MockWarnings', (object,), {'warn': lambda msg: print(msg)})() # pragma: no cover

def exception_type_from_error_code(error_code): return ValueError # pragma: no cover
error_code = 404 # pragma: no cover
node_def = 'example_node_def' # pragma: no cover
op = 'example_operation' # pragma: no cover
message = 'An error occurred during execution' # pragma: no cover
class UnknownError(Exception):# pragma: no cover
    def __init__(self, node_def, op, message, error_code):# pragma: no cover
        super().__init__(message)# pragma: no cover
        self.node_def = node_def# pragma: no cover
        self.op = op# pragma: no cover
        self.error_code = error_code # pragma: no cover
warnings = type('MockWarnings', (object,), {'warn': lambda msg: print(msg)})() # pragma: no cover

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
