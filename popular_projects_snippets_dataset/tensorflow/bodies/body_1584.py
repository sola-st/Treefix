# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32,
    tensor_array_name="foo",
    size=3,
    infer_shape=False)
exit(ta.split(1.0, [1]).flow)
