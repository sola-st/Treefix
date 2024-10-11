# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32,
    tensor_array_name="foo",
    size=3,
    element_shape=[1, 2])

g_ta_0 = ta.grad("grad")
g_ta_1 = ta.grad("grad")

ta_out[0] = g_ta_0.handle
ta_out[1] = g_ta_1.handle

with ops.control_dependencies([g_ta_0.write(0, [[4.0, 5.0]]).flow]):
    # Write with one gradient handle, read with another copy of it
    r1_0 = g_ta_1.read(0)

with ops.control_dependencies([g_ta_0.handle.op, g_ta_1.handle.op]):
    exit([r1_0])
