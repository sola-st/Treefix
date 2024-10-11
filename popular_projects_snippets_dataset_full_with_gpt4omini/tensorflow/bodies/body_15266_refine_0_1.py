from typing import List # pragma: no cover

class MockRowPartition:# pragma: no cover
    def __init__(self, lengths):# pragma: no cover
        self.lengths = lengths# pragma: no cover
# pragma: no cover
    def is_uniform(self):# pragma: no cover
        return len(set(self.lengths)) == 1# pragma: no cover
# pragma: no cover
    def row_lengths(self):# pragma: no cover
        return self.lengths# pragma: no cover
# pragma: no cover
    @classmethod# pragma: no cover
    def from_row_lengths(cls, lengths):# pragma: no cover
        return cls(lengths)# pragma: no cover
# pragma: no cover
    @classmethod# pragma: no cover
    def from_uniform_row_length(cls, uniform_length, nvals, nrows):# pragma: no cover
        return cls([uniform_length] * nrows)# pragma: no cover
# pragma: no cover
    def uniform_row_length(self):# pragma: no cover
        return self.lengths[0] if self.is_uniform() else None # pragma: no cover
class MockSelf:# pragma: no cover
    def broadcast_tensor(self, lengths):# pragma: no cover
        return [length * 2 for length in lengths]# pragma: no cover
# pragma: no cover
    def dest_nrows(self):# pragma: no cover
        return 5 # pragma: no cover
rp = MockRowPartition([3, 3, 3]) # pragma: no cover
self = MockSelf() # pragma: no cover

from typing import List # pragma: no cover

class RowPartition:# pragma: no cover
    def __init__(self, lengths):# pragma: no cover
        self.lengths = lengths# pragma: no cover
# pragma: no cover
    def is_uniform(self):# pragma: no cover
        return len(set(self.lengths)) == 1# pragma: no cover
# pragma: no cover
    def row_lengths(self):# pragma: no cover
        return self.lengths# pragma: no cover
# pragma: no cover
    @classmethod# pragma: no cover
    def from_row_lengths(cls, lengths):# pragma: no cover
        return cls(lengths)# pragma: no cover
# pragma: no cover
    @classmethod# pragma: no cover
    def from_uniform_row_length(cls, uniform_length, nvals, nrows):# pragma: no cover
        return cls([uniform_length] * nrows)# pragma: no cover
# pragma: no cover
    def uniform_row_length(self):# pragma: no cover
        return self.lengths[0] if self.is_uniform() else None # pragma: no cover
class MockSelf:# pragma: no cover
    def broadcast_tensor(self, lengths):# pragma: no cover
        return [length * 2 for length in lengths]# pragma: no cover
# pragma: no cover
    def dest_nrows(self):# pragma: no cover
        return 5 # pragma: no cover
rp = RowPartition([3, 3, 3]) # pragma: no cover
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
