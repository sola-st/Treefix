class MockRowPartition: # pragma: no cover
    def __init__(self, nrows, nvals, is_uniform=True): # pragma: no cover
        self._nrows = nrows # pragma: no cover
        self._nvals = nvals # pragma: no cover
        self._is_uniform = is_uniform # pragma: no cover
    def nrows(self): # pragma: no cover
        return self._nrows # pragma: no cover
    def nvals(self): # pragma: no cover
        return self._nvals # pragma: no cover
    def is_uniform(self): # pragma: no cover
        return self._is_uniform # pragma: no cover
 # pragma: no cover
class DynamicRaggedShape: # pragma: no cover
    def __init__(self, row_partitions, inner_shape, static_inner_shape=None, validate=False): # pragma: no cover
        self.row_partitions = row_partitions # pragma: no cover
        self.inner_shape = inner_shape # pragma: no cover
        self.static_inner_shape = static_inner_shape # pragma: no cover
        self.validate = validate # pragma: no cover
        self.num_row_partitions = len(row_partitions) # pragma: no cover
        self.rank = len(inner_shape) + len(row_partitions) if inner_shape else None # pragma: no cover
 # pragma: no cover
    @staticmethod # pragma: no cover
    def _from_inner_shape(inner_shape): # pragma: no cover
        return DynamicRaggedShape([], inner_shape) # pragma: no cover
 # pragma: no cover
    def _slice_shape(self, start, stop): # pragma: no cover
        new_row_partitions = self.row_partitions[start:stop] # pragma: no cover
        new_inner_shape = self.inner_shape[:stop - start] # pragma: no cover
        return DynamicRaggedShape(new_row_partitions, new_inner_shape) # pragma: no cover
 # pragma: no cover
    def _with_num_row_partitions(self, num): # pragma: no cover
        if num != 0: # pragma: no cover
            raise NotImplementedError('__getitem__[start:stop] where start > 0 not implemented') # pragma: no cover
        return DynamicRaggedShape([], self.inner_shape[num:]) # pragma: no cover
 # pragma: no cover
self = DynamicRaggedShape([MockRowPartition(5, 10)], [10, 20, 30], validate=False) # pragma: no cover
start = 0 # pragma: no cover
stop = 5 # pragma: no cover

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
    _l_(18817)

    aux = DynamicRaggedShape._from_inner_shape([])
    _l_(18791)
    exit(aux)
elif start == 0:
    _l_(18816)

    if stop <= self.num_row_partitions:
        _l_(18806)

        if stop == 1:
            _l_(18793)

            aux = DynamicRaggedShape._from_inner_shape(
                [self.row_partitions[0].nrows()])
            _l_(18792)
            exit(aux)
        new_row_partitions = self.row_partitions[:stop - 1]
        _l_(18794)
        new_inner_shape = [new_row_partitions[-1].nvals()]
        _l_(18795)
        aux = DynamicRaggedShape(new_row_partitions, new_inner_shape)
        _l_(18796)
        exit(aux)
    else:
        if self.rank is None:
            _l_(18802)

            new_inner_rank = stop - self.num_row_partitions
            _l_(18797)
            new_inner_shape = self.inner_shape[:new_inner_rank]
            _l_(18798)
            aux = DynamicRaggedShape(
                row_partitions=self.row_partitions,
                inner_shape=new_inner_shape,
                static_inner_shape=None,
                validate=False)
            _l_(18799)
            exit(aux)

        elif self.rank <= stop:
            _l_(18801)

            aux = self
            _l_(18800)
            exit(aux)
        new_inner_rank = stop - self.num_row_partitions
        _l_(18803)
        new_inner_shape = self.inner_shape[:new_inner_rank]
        _l_(18804)
        aux = DynamicRaggedShape(
            row_partitions=self.row_partitions,
            inner_shape=new_inner_shape,
            static_inner_shape=tensor_shape.TensorShape([None] *
                                                        new_inner_rank),
            validate=False)
        _l_(18805)
        exit(aux)
else:
    if self.rank is None or stop < self.rank:
        _l_(18809)

        partial = self._slice_shape(0, stop)
        _l_(18807)
    else:
        partial = self
        _l_(18808)

    for x in partial.row_partitions:
        _l_(18812)

        if not x.is_uniform():
            _l_(18811)

            raise ValueError("All relevant dimensions must be uniform")
            _l_(18810)
    if partial.rank is None:
        _l_(18814)

        # TODO(martinz): Implement _with_num_row_partitions(0) if rank is
        # unknown, and remove.
        raise NotImplementedError(
            "__getitem__[start:stop] where start > 0 not implemented")
        _l_(18813)
    aux = DynamicRaggedShape._from_inner_shape(
        partial._with_num_row_partitions(0).inner_shape[start:])
    _l_(18815)

    exit(aux)
