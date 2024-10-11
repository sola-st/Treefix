from typing import Any # pragma: no cover
class gen_io_ops: # pragma: no cover
    @staticmethod # pragma: no cover
    def identity_reader_v2(name: Any = None): # pragma: no cover
        return 'some_reader_resource' # pragma: no cover

name = 'default_name' # pragma: no cover
class IdentityReader: # pragma: no cover
    def __init__(self, rr, supports_serialize: bool): # pragma: no cover
        self.rr = rr # pragma: no cover
        self.supports_serialize = supports_serialize # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
from l3.Runtime import _l_
"""Create a IdentityReader.

    Args:
      name: A name for the operation (optional).
    """
rr = gen_io_ops.identity_reader_v2(name=name)
_l_(22064)
super(IdentityReader, self).__init__(rr, supports_serialize=True)
_l_(22065)
