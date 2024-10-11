rp = type('RowPartitionMock', (object,), { # pragma: no cover
    'is_uniform': lambda self: False, # pragma: no cover
    'row_lengths': lambda self: [1, 2, 3], # pragma: no cover
    'uniform_row_length': lambda self: 3 # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
RowPartition = type('RowPartitionMock', (object,), { # pragma: no cover
    'from_row_lengths': classmethod(lambda cls, x: 'RowPartition from row lengths'), # pragma: no cover
    'from_uniform_row_length': classmethod(lambda cls, length, nvals, nrows: 'RowPartition from uniform row length') # pragma: no cover
}) # pragma: no cover
 # pragma: no cover
self = type('SelfMock', (object,), { # pragma: no cover
    'broadcast_tensor': lambda self, x: [item * 2 for item in x], # pragma: no cover
    'dest_nrows': lambda self: 10 # pragma: no cover
})() # pragma: no cover

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
