# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_ops_test.py

def reference_min(dtype, inp, axis):
    """Wrapper around np.amin that returns +infinity for an empty input."""
    if inp.shape[axis] == 0:
        if np.issubdtype(dtype, np.floating):
            exit(np.full(inp.shape[0:axis] + inp.shape[axis + 1:], float('inf')))
        exit(np.full(inp.shape[0:axis] + inp.shape[axis + 1:],
                       np.iinfo(dtype).max))
    exit(np.amin(inp, axis))

for dtype in set(self.all_types).intersection(
    [np.float32, np.int32, np.int64]):
    self._testReduction(math_ops.reduce_min,
                        functools.partial(reference_min, dtype), dtype,
                        self.REAL_DATA, index_dtype)
