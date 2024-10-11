import numpy as np # pragma: no cover

class MockRowPartition: # pragma: no cover
    def __init__(self, uniform=False): # pragma: no cover
        self._row_lengths = np.array([3, 3, 3]) if uniform else np.array([2, 3, 4]) # pragma: no cover
    def is_uniform(self): # pragma: no cover
        return len(set(self._row_lengths)) == 1 # pragma: no cover
    def row_lengths(self): # pragma: no cover
        return self._row_lengths # pragma: no cover
    def uniform_row_length(self): # pragma: no cover
        if self.is_uniform(): # pragma: no cover
            return self._row_lengths[0] # pragma: no cover
        raise ValueError('Row lengths are not uniform.') # pragma: no cover
    @classmethod # pragma: no cover
    def from_row_lengths(cls, row_lengths): # pragma: no cover
        instance = cls() # pragma: no cover
        instance._row_lengths = row_lengths # pragma: no cover
        return instance # pragma: no cover
    @classmethod # pragma: no cover
    def from_uniform_row_length(cls, row_length, nvals, nrows): # pragma: no cover
        instance = cls(True) # pragma: no cover
        instance._row_lengths = np.full((nrows,), row_length) # pragma: no cover
        return instance # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def broadcast_tensor(self, tensor): # pragma: no cover
        return np.broadcast_to(tensor, (len(tensor),)) # pragma: no cover
    def dest_nrows(self): # pragma: no cover
        return 3 # pragma: no cover
 # pragma: no cover
rp = MockRowPartition() # pragma: no cover
RowPartition = MockRowPartition # pragma: no cover
self = MockSelf() # pragma: no cover

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
