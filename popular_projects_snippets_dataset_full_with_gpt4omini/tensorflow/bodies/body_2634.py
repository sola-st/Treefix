# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py

def _TransposeAndTest(array, permutation):
    c = self._NewComputation()
    ops.Transpose(ops.Constant(c, array), permutation)
    expected = np.transpose(array, permutation)
    self._ExecuteAndCompareClose(c, expected=[expected])

_TransposeAndTest(NumpyArrayF32([[1, 2, 3], [4, 5, 6]]), [0, 1])
_TransposeAndTest(NumpyArrayF32([[1, 2, 3], [4, 5, 6]]), [1, 0])
_TransposeAndTest(NumpyArrayF32([[1, 2], [4, 5]]), [0, 1])
_TransposeAndTest(NumpyArrayF32([[1, 2], [4, 5]]), [1, 0])

arr = np.random.RandomState(0).randn(2, 3, 4).astype(np.float32)
for permutation in itertools.permutations(range(arr.ndim)):
    _TransposeAndTest(arr, permutation)
    _TransposeAndTest(np.asfortranarray(arr), permutation)
