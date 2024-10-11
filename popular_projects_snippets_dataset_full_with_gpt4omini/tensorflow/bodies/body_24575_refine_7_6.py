from unittest.mock import Mock # pragma: no cover

context = Mock() # pragma: no cover
grpc = Mock() # pragma: no cover
grpc.StatusCode = Mock() # pragma: no cover
grpc.StatusCode.UNIMPLEMENTED = 'UNIMPLEMENTED' # pragma: no cover

class MockStatusCode: UNIMPLEMENTED = 'UNIMPLEMENTED' # pragma: no cover
grpc = type('MockGrpc', (), {'StatusCode': MockStatusCode})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_service_pb2_grpc.py
from l3.Runtime import _l_
"""Send a collection of source code files being debugged.
    """
context.set_code(grpc.StatusCode.UNIMPLEMENTED)
_l_(9841)
context.set_details('Method not implemented!')
_l_(9842)
raise NotImplementedError('Method not implemented!')
_l_(9843)
