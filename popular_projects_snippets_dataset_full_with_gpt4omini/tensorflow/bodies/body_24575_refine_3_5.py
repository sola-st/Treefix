from unittest.mock import MagicMock # pragma: no cover

context = MagicMock() # pragma: no cover
grpc = type('MockGrpc', (object,), {'StatusCode': type('MockStatusCode', (object,), {'UNIMPLEMENTED': 12})})() # pragma: no cover

class MockContext: # pragma: no cover
    def set_code(self, code): pass # pragma: no cover
    def set_details(self, details): pass # pragma: no cover

context = MockContext() # pragma: no cover
grpc = type('MockGrpc', (object,), {'StatusCode': type('MockStatusCode', (object,), {'UNIMPLEMENTED': 12})})() # pragma: no cover
def mock_method(): pass # pragma: no cover
context.set_code = mock_method # pragma: no cover
context.set_details = mock_method # pragma: no cover

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
