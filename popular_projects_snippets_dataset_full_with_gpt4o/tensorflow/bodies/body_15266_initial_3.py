import numpy as np # pragma: no cover

rp = type('MockRP', (object,), {'is_uniform': lambda s: True, 'row_lengths': lambda s: np.array([3, 3, 3]), 'uniform_row_length': lambda s: 3})() # pragma: no cover
RowPartition = type('MockRowPartition', (object,), {'from_row_lengths': staticmethod(lambda lengths: 'Broadcasted RowPartition with lengths {}'.format(lengths)), 'from_uniform_row_length': staticmethod(lambda length, nvals, nrows: 'Uniform RowPartition with length {}, nvals {}, nrows {}'.format(length, nvals, nrows))}) # pragma: no cover
self = type('MockSelf', (object,), {'broadcast_tensor': lambda s, lengths: lengths * 2, 'dest_nrows': lambda s: 3})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
from l3.Runtime import _l_
"""Return a new shape where the rows are broadcasted.

        *--self--->*
        |          |
        rp       result
        |          |
        V          V
        *--------->*

    This is equivalent to:
      return RowPartition.from_row_lengths(self.broadcast(rp.row_lengths()))

    However, if the shape has uniform row length, then that property is
    maintained.

    Args:
      rp: a row partition.

    Returns:
      a RowPartition representing a broadcast version of this row partition.
    """
if not rp.is_uniform():
    _l_(20199)

    aux = RowPartition.from_row_lengths(
        self.broadcast_tensor(rp.row_lengths()))
    _l_(20197)
    exit(aux)
else:
    aux = RowPartition.from_uniform_row_length(
        rp.uniform_row_length(),
        nvals=rp.uniform_row_length() * self.dest_nrows(),
        nrows=self.dest_nrows())
    _l_(20198)
    exit(aux)
