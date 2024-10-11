gen_io_ops = type('MockGenIoOps', (object,), {'identity_reader_v2': lambda name=None: 'identity_reader_output'})() # pragma: no cover
name = 'MyIdentityReader' # pragma: no cover
IdentityReader = type('IdentityReader', (object,), {'__init__': lambda self, rr, supports_serialize: None}) # pragma: no cover

gen_io_ops = type('MockGenIoOps', (object,), {'identity_reader_v2': lambda name: 'identity_reader_output'})() # pragma: no cover
name = 'MyIdentityReader' # pragma: no cover
class IdentityReader: # pragma: no cover
    def __init__(self, rr, supports_serialize): pass # pragma: no cover
self = IdentityReader(rr='dummy_rr', supports_serialize=True) # pragma: no cover

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
