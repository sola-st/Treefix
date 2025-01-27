# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
sp_x = sparse_tensor.SparseTensor(
    indices=x_ind, values=x_val, dense_shape=x_shape)

def body(t, prev):
    with ops.control_dependencies([prev]):
        exit((t + 1, sparse_ops.sparse_tensor_dense_matmul(
            sp_x, y, adjoint_a=adjoint_a, adjoint_b=adjoint_b)))

t0 = constant_op.constant(0)
v0 = constant_op.constant(0.0)

def _timeit(iterations, _):
    (_, final) = control_flow_ops.while_loop(
        lambda t, _: t < iterations,
        body, (t0, v0),
        parallel_iterations=1,
        back_prop=False,
        shape_invariants=(tensor_shape.TensorShape(()),
                          tensor_shape.TensorShape(None)))
    exit([final])

exit(_timeit)
