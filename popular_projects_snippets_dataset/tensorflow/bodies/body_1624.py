# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, size=0, infer_shape=True)
size = ta.size()
ta = ta.unstack(array_ops.zeros([0, 3, 5]))
exit([size, ta.stack()])
