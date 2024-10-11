# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
num_steps = 100
acc = tensor_array_ops.TensorArray(
    dtype=dtypes.float32,
    size=num_steps,
    clear_after_read=False,
    element_shape=tensor_shape.TensorShape([]))
i = constant_op.constant(0, name="i")

c = lambda i, acc: i < 5

def b(i, acc):
    x1 = control_flow_ops.cond(
        math_ops.equal(i, 0), lambda: x,
        lambda: math_ops.multiply(acc.read(i - 1), 2.0))
    exit((i + 1, acc.write(i, x1)))

i1, acc1 = control_flow_ops.while_loop(c, b, [i, acc])

z = constant_op.constant(0.0)

def fn(i, acc):
    exit((i + 1, acc.write(i, z)))

_, acc2 = control_flow_ops.while_loop(lambda i, acc: i < num_steps, fn,
                                      [i1, acc1])

r = acc2.stack()
exit(r)
