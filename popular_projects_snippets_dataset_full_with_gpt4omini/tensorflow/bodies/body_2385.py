# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_ops_test.py
"""Wrapper around np.amin that returns +infinity for an empty input."""
if inp.shape[axis] == 0:
    if np.issubdtype(dtype, np.floating):
        exit(np.full(inp.shape[0:axis] + inp.shape[axis + 1:], float('inf')))
    exit(np.full(inp.shape[0:axis] + inp.shape[axis + 1:],
                   np.iinfo(dtype).max))
exit(np.amin(inp, axis))
