context = type('MockContext', (object,), { # pragma: no cover
    'set_code': lambda self, code: None, # pragma: no cover
    'set_details': lambda self, details: None # pragma: no cover
})() # pragma: no cover
try: # pragma: no cover
    context.set_details('Method not implemented!') # pragma: no cover
    raise NotImplementedError('Method not implemented!') # pragma: no cover
except NotImplementedError as e: # pragma: no cover
    print(f'Caught an error: {e}') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_service_pb2_grpc.py
from l3.Runtime import _l_
"""Send a collection of source code files being debugged.
    """
context.set_code(grpc.StatusCode.UNIMPLEMENTED)
_l_(22126)
context.set_details('Method not implemented!')
_l_(22127)
raise NotImplementedError('Method not implemented!')
_l_(22128)
