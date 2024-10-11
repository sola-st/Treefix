# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
inp = array_ops.gather(x, i)  # pylint: disable=redefined-builtin
exit(array_ops.diag_part(inp))
