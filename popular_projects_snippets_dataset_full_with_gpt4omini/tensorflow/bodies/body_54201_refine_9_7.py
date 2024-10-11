def exception_type_from_error_code(code): return ValueError if code == 100 else KeyError # pragma: no cover
error_code = 100 # pragma: no cover
node_def = 'SampleNode' # pragma: no cover
op = 'SampleOperation' # pragma: no cover
message = 'An error has occurred.' # pragma: no cover
class UnknownError(Exception): pass # pragma: no cover
warnings = type('MockWarnings', (object,), {'warn': lambda msg: print(msg)})() # pragma: no cover

import warnings # pragma: no cover
import sys # pragma: no cover

def exception_type_from_error_code(code): return ValueError if code == 404 else RuntimeError # pragma: no cover
error_code = 404 # pragma: no cover
node_def = {'name': 'SampleNode'} # pragma: no cover
op = 'SampleOperation' # pragma: no cover
message = 'An error has occurred.' # pragma: no cover
class UnknownError(Exception): pass # pragma: no cover
sys.exit = lambda x: print(f'Exiting with code: {x}') # pragma: no cover
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
