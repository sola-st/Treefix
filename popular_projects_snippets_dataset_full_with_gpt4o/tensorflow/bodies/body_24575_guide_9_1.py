class MockContext: # pragma: no cover
    def set_code(self, code): # pragma: no cover
        self.code = code # pragma: no cover
    def set_details(self, details): # pragma: no cover
        self.details = details # pragma: no cover
context = MockContext() # pragma: no cover
context.set_details('Method not implemented!') # pragma: no cover

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
