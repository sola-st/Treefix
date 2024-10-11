from unittest.mock import Mock # pragma: no cover
import types # pragma: no cover

gen_io_ops = type('MockGenIOOps', (object,), {'identity_reader_v2': Mock(return_value='mock_rr')})() # pragma: no cover
name = 'example_name' # pragma: no cover
IdentityReader = Mock() # pragma: no cover
self = Mock() # pragma: no cover

from unittest.mock import Mock # pragma: no cover

gen_io_ops = type('MockGenIOOps', (object,), {'identity_reader_v2': Mock(return_value='mock_rr')})() # pragma: no cover
name = 'example_name' # pragma: no cover
class IdentityReaderBase:# pragma: no cover
    def __init__(self, rr, supports_serialize):# pragma: no cover
        self.rr = rr# pragma: no cover
        self.supports_serialize = supports_serialize # pragma: no cover
class IdentityReader(IdentityReaderBase):# pragma: no cover
    def __init__(self, rr, supports_serialize=True):# pragma: no cover
        super(IdentityReader, self).__init__(rr, supports_serialize) # pragma: no cover
self = IdentityReader('mock_rr') # pragma: no cover

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
