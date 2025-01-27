# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
diagonal = array_ops.gather(x, i)
exit(array_ops.matrix_diag(
    diagonal, k=(0, 1), num_rows=4, num_cols=5, align="RIGHT_LEFT"))
