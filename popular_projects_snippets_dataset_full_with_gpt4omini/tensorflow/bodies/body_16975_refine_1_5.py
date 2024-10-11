gen_io_ops = type('MockGenIOOps', (), {'identity_reader_v2': lambda name: 'identity_reader'})() # pragma: no cover
name = 'MyIdentityReader' # pragma: no cover

class MockGenIOOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def identity_reader_v2(name): # pragma: no cover
        return 'identity_reader_output' # pragma: no cover
 # pragma: no cover
class IdentityReader: # pragma: no cover
    def __init__(self, rr, supports_serialize): # pragma: no cover
        self.rr = rr # pragma: no cover
        self.supports_serialize = supports_serialize # pragma: no cover

gen_io_ops = MockGenIOOps() # pragma: no cover
name = 'MyIdentityReader' # pragma: no cover
rr = gen_io_ops.identity_reader_v2(name=name) # pragma: no cover
self = IdentityReader(rr, supports_serialize=True) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
from l3.Runtime import _l_
"""Create a IdentityReader.

    Args:
      name: A name for the operation (optional).
    """
rr = gen_io_ops.identity_reader_v2(name=name)
_l_(9750)
super(IdentityReader, self).__init__(rr, supports_serialize=True)
_l_(9751)
