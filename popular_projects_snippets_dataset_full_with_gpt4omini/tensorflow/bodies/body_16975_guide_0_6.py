name = 'identity_reader_example' # pragma: no cover
IdentityReader = type('IdentityReader', (object,), {}) # pragma: no cover

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
