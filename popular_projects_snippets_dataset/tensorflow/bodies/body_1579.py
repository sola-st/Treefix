# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtype1, tensor_array_name="foo", size=3)

w0 = ta.write(0, math_ops.cast([[4.0, 5.0]], dtype1))

# Test reading wrong datatype.
exit(gen_data_flow_ops.tensor_array_read_v3(
    handle=w0.handle, index=0, dtype=dtype2, flow_in=w0.flow))
