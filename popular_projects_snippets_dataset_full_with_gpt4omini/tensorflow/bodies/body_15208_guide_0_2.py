class DynamicRaggedShape: # pragma: no cover
    def __init__(self, row_partitions, inner_shape, static_inner_shape=None, validate=True): # pragma: no cover
        self.row_partitions = row_partitions # pragma: no cover
        self.inner_shape = inner_shape # pragma: no cover
        self.static_inner_shape = static_inner_shape # pragma: no cover
        self.validate = validate # pragma: no cover
        self.num_row_partitions = len(row_partitions) if row_partitions else 0 # pragma: no cover
        self.rank = len(inner_shape) if inner_shape else None # pragma: no cover
    @staticmethod # pragma: no cover
    def _from_inner_shape(inner_shape): # pragma: no cover
        return DynamicRaggedShape([], inner_shape) # pragma: no cover
    def is_uniform(self): # pragma: no cover
        return all(partition.is_uniform() for partition in self.row_partitions) if self.row_partitions else True # pragma: no cover
class RowPartition: # pragma: no cover
    def __init__(self, nrows, nvals): # pragma: no cover
        self._nrows = nrows # pragma: no cover
        self._nvals = nvals # pragma: no cover
    def nrows(self): # pragma: no cover
        return self._nrows # pragma: no cover
    def nvals(self): # pragma: no cover
        return self._nvals # pragma: no cover
    def is_uniform(self): # pragma: no cover
        return True # pragma: no cover

self = DynamicRaggedShape([RowPartition(5, 10), RowPartition(5, 10)], [3, 3]) # pragma: no cover
start = 1 # pragma: no cover
stop = 2 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
from l3.Runtime import _l_
"""Returns a shape self[start:stop].

    If start == 0, then this truncates dimensions after stop.
    If start != 0, then this will return a shape with num_row_partitions == 0.

    See __getitem__.

    Args:
      start: the first dimension. 0 <= start <= rank
      stop: the last dimension (exclusive). 0 <= stop <= rank
    """
if stop <= start:
    _l_(6354)

    aux = DynamicRaggedShape._from_inner_shape([])
    _l_(6328)
    exit(aux)
elif start == 0:
    _l_(6353)

    if stop <= self.num_row_partitions:
        _l_(6343)

        if stop == 1:
            _l_(6330)

            aux = DynamicRaggedShape._from_inner_shape(
                [self.row_partitions[0].nrows()])
            _l_(6329)
            exit(aux)
        new_row_partitions = self.row_partitions[:stop - 1]
        _l_(6331)
        new_inner_shape = [new_row_partitions[-1].nvals()]
        _l_(6332)
        aux = DynamicRaggedShape(new_row_partitions, new_inner_shape)
        _l_(6333)
        exit(aux)
    else:
        if self.rank is None:
            _l_(6339)

            new_inner_rank = stop - self.num_row_partitions
            _l_(6334)
            new_inner_shape = self.inner_shape[:new_inner_rank]
            _l_(6335)
            aux = DynamicRaggedShape(
                row_partitions=self.row_partitions,
                inner_shape=new_inner_shape,
                static_inner_shape=None,
                validate=False)
            _l_(6336)
            exit(aux)

        elif self.rank <= stop:
            _l_(6338)

            aux = self
            _l_(6337)
            exit(aux)
        new_inner_rank = stop - self.num_row_partitions
        _l_(6340)
        new_inner_shape = self.inner_shape[:new_inner_rank]
        _l_(6341)
        aux = DynamicRaggedShape(
            row_partitions=self.row_partitions,
            inner_shape=new_inner_shape,
            static_inner_shape=tensor_shape.TensorShape([None] *
                                                        new_inner_rank),
            validate=False)
        _l_(6342)
        exit(aux)
else:
    if self.rank is None or stop < self.rank:
        _l_(6346)

        partial = self._slice_shape(0, stop)
        _l_(6344)
    else:
        partial = self
        _l_(6345)

    for x in partial.row_partitions:
        _l_(6349)

        if not x.is_uniform():
            _l_(6348)

            raise ValueError("All relevant dimensions must be uniform")
            _l_(6347)
    if partial.rank is None:
        _l_(6351)

        # TODO(martinz): Implement _with_num_row_partitions(0) if rank is
        # unknown, and remove.
        raise NotImplementedError(
            "__getitem__[start:stop] where start > 0 not implemented")
        _l_(6350)
    aux = DynamicRaggedShape._from_inner_shape(
        partial._with_num_row_partitions(0).inner_shape[start:])
    _l_(6352)

    exit(aux)
