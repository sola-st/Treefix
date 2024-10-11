from typing import List, Union # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.dest_nrows = lambda: 3 # pragma: no cover
self.broadcast_tensor = lambda x: [i * 2 for i in x] # pragma: no cover
class RowPartition: # pragma: no cover
    def __init__(self, lengths: List[int]): # pragma: no cover
        self.lengths = lengths # pragma: no cover
    @classmethod # pragma: no cover
    def from_row_lengths(cls, lengths): # pragma: no cover
        return cls(lengths) # pragma: no cover
    @classmethod # pragma: no cover
    def from_uniform_row_length(cls, length, nvals, nrows): # pragma: no cover
        return cls([length] * nrows) # pragma: no cover
    def is_uniform(self): # pragma: no cover
        return len(set(self.lengths)) == 1 # pragma: no cover
    def row_lengths(self): # pragma: no cover
        return self.lengths # pragma: no cover
    def uniform_row_length(self): # pragma: no cover
        return self.lengths[0] if self.is_uniform() else None # pragma: no cover
rp = RowPartition([4, 4, 4]) # pragma: no cover

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
    _l_(7206)

    aux = RowPartition.from_row_lengths(
        self.broadcast_tensor(rp.row_lengths()))
    _l_(7204)
    exit(aux)
else:
    aux = RowPartition.from_uniform_row_length(
        rp.uniform_row_length(),
        nvals=rp.uniform_row_length() * self.dest_nrows(),
        nrows=self.dest_nrows())
    _l_(7205)
    exit(aux)
