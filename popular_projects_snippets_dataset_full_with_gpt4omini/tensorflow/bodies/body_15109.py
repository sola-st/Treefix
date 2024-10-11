# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py

def func(x, i):
    rt1 = RaggedTensor.from_row_splits(
        values=x, row_splits=[0, 2, 2, 4, 7, 7, 8])
    rt2 = rt1 * [[10], [20], [30], [40], [50], [60]]
    v_slice = rt2._to_variant(batched_input=True)[i]
    exit(RaggedTensor._from_variant(
        v_slice, dtype=rt2.dtype, output_ragged_rank=0))

self._testGradient(
    functools.partial(func, i=0), [3.0, 1.0, 4.0, 1.0, 1.0, 0.0, 2.0, 1.0],
    [10., 10., 0., 0., 0., 0., 0., 0.])
self._testGradient(
    functools.partial(func, i=1), [3.0, 1.0, 4.0, 1.0, 1.0, 0.0, 2.0, 1.0],
    [0., 0., 0., 0., 0., 0., 0., 0.])
self._testGradient(
    functools.partial(func, i=2), [3.0, 1.0, 4.0, 1.0, 1.0, 0.0, 2.0, 1.0],
    [0., 0., 30., 30., 0., 0., 0., 0.])
self._testGradient(
    functools.partial(func, i=3), [3.0, 1.0, 4.0, 1.0, 1.0, 0.0, 2.0, 1.0],
    [0., 0., 0., 0., 40., 40., 40., 0.])
self._testGradient(
    functools.partial(func, i=4), [3.0, 1.0, 4.0, 1.0, 1.0, 0.0, 2.0, 1.0],
    [0., 0., 0., 0., 0., 0., 0., 0.])
self._testGradient(
    functools.partial(func, i=5), [3.0, 1.0, 4.0, 1.0, 1.0, 0.0, 2.0, 1.0],
    [0., 0., 0., 0., 0., 0., 0., 60.])
