# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtype1, tensor_array_name="foo", size=3)

w0 = ta.write(0, math_ops.cast([[4.0, 5.0]], dtype1))

# Test reading from a different index than the one we wrote to
with ops.control_dependencies([w0.read(1)]):
    exit(1.0)
