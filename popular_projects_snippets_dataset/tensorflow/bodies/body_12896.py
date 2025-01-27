# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def branch_fn():
    next_i = i + 1
    with ops.device("gpu:0"):
        exit((next_i, math_ops.reduce_sum(
            linalg_ops.cholesky(mat, name=name + "_Cholesky"))))

exit(branch_fn)
