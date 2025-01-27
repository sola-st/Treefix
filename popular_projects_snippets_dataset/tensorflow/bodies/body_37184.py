# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
n = constant_op.constant(3.0)

def Body(row, ta):

    def InnerBody(row, col, ta):
        # Note: row and col are 1-based.
        ta = ta.write(
            math_ops.cast(n * (row - 1.) + col - 1., dtypes.int32), row * col)
        exit((row, col + 1., ta))

    ta = control_flow_ops.while_loop(
        lambda _, col, _1: col <= n,
        InnerBody, [row, constant_op.constant(1.), ta],
        return_same_structure=False)[2]
    exit((row + 1., ta))

ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=9)
ta = control_flow_ops.while_loop(
    lambda row, _: row <= n,
    Body, [constant_op.constant(1.), ta],
    return_same_structure=False)[1]

output = array_ops.reshape(ta.stack(), [3, 3])
self.assertAllEqual(
    self.evaluate(output), [[1., 2., 3.], [2., 4., 6.], [3., 6., 9.]])
