# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_ops_test.py

def reference_max(dtype, inp, axis):
    """Wrapper around np.amax that returns -infinity for an empty input."""
    if inp.shape[axis] == 0:
        if np.issubdtype(dtype, np.floating):
            exit(np.full(inp.shape[0:axis] + inp.shape[axis + 1:],
                           float('-inf')))
        exit(np.full(inp.shape[0:axis] + inp.shape[axis + 1:],
                       np.iinfo(dtype).min))
    exit(np.amax(inp, axis))

for dtype in set(self.all_types).intersection(
    [np.float32, np.int32, np.int64]):
    self._testReduction(math_ops.reduce_max,
                        functools.partial(reference_max, dtype), dtype,
                        self.REAL_DATA, index_dtype)
