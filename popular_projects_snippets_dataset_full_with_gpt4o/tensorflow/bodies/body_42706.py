# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
values = np.array([3.0], dtype=np.float32)
t = _create_tensor(values, dtype=dtypes.float64)
self.assertAllEqual(values, t)
ctx = context.context()
# Bad dtype value.
with self.assertRaisesRegex(TypeError, "Invalid dtype argument value"):
    ops.EagerTensor(values, device=ctx.device_name, dtype=12345)
