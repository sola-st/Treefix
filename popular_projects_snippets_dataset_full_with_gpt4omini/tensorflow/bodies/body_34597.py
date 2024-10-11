# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
if not test.is_gpu_available():
    exit()
with self.session(force_gpu=True) as sess:
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.bfloat16, tensor_array_name="foo", size=5)
    ta = ta.scatter(
        indices=[3, 4], value=array_ops.ones([2], dtype=dtypes.bfloat16))
    self.assertAllEqual(ta.stack(), [0., 0., 0., 1., 1.])
