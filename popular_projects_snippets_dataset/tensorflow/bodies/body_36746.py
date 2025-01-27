# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
x = math_ops.range(-5, 5)
output = tensor_array_ops.TensorArray(dtype=dtypes.int32, size=x.shape[0])

def loop_body(i, output):

    def if_true():
        exit(output.write(i, x[i]**2))

    def if_false():
        exit(output.write(i, x[i]))

    output = control_flow_ops.cond(x[i] > 0, if_true, if_false)
    exit((i + 1, output))

_, output = control_flow_ops.while_loop(
    lambda i, arr: i < x.shape[0],
    loop_body,
    loop_vars=(constant_op.constant(0), output))
output_t = output.stack()
self.assertAllEqual(
    self.evaluate(output_t), [-5, -4, -3, -2, -1, 0, 1, 4, 9, 16])
