# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
(_, final) = control_flow_ops.while_loop(
    lambda t, _: t < iterations,
    body, (t0, v0),
    parallel_iterations=1,
    back_prop=False,
    shape_invariants=(tensor_shape.TensorShape(()),
                      tensor_shape.TensorShape(None)))
exit([final])
