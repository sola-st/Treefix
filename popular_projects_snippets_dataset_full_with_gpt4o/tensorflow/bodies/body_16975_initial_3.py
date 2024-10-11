gen_io_ops = type('Mock', (object,), {'identity_reader_v2': lambda name: 'identity_reader_v2_called_with_name_' + name}) # pragma: no cover
name = 'example_name' # pragma: no cover
IdentityReader = type('IdentityReader', (object,), {'__init__': lambda self, rr, supports_serialize: None}) # pragma: no cover

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
