from typing import List, Callable # pragma: no cover

class MockRowPartition:# pragma: no cover
    def __init__(self, row_lengths=None, uniform_length=None, nrows=None):# pragma: no cover
        self.row_lengths = row_lengths or []# pragma: no cover
        self.uniform_length = uniform_length# pragma: no cover
        self.nrows = nrows or 0# pragma: no cover
# pragma: no cover
    def is_uniform(self):# pragma: no cover
        return self.uniform_length is not None# pragma: no cover
# pragma: no cover
    @classmethod# pragma: no cover
    def from_row_lengths(cls, row_lengths):# pragma: no cover
        return cls(row_lengths=row_lengths)# pragma: no cover
# pragma: no cover
    @classmethod# pragma: no cover
    def from_uniform_row_length(cls, uniform_length, nvals, nrows):# pragma: no cover
        return cls(uniform_length=uniform_length, nrows=nrows)# pragma: no cover
# pragma: no cover
    def row_lengths(self):# pragma: no cover
        return self.row_lengths# pragma: no cover
# pragma: no cover
    def uniform_row_length(self):# pragma: no cover
        return self.uniform_length # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self, dest_nrows):# pragma: no cover
        self.dest_nrows = dest_nrows# pragma: no cover
# pragma: no cover
    def broadcast_tensor(self, lengths):# pragma: no cover
        return lengths  # Mock implementation simply returns input lengths# pragma: no cover
# pragma: no cover
rp = MockRowPartition(row_lengths=[1, 2, 3], uniform_length=None)# pragma: no cover
self = MockSelf(dest_nrows=5) # pragma: no cover

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
