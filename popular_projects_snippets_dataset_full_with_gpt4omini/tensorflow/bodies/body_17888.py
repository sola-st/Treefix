# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
input = array_ops.gather(x, i)  # pylint: disable=redefined-builtin
exit(array_ops.matrix_diag_part(
    input, k=(-2, 0), padding_value=3, align="RIGHT_LEFT"))
