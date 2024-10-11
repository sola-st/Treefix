# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
x = ops.convert_to_tensor([
    np.array(321, dtype=np.int64).item(),
    np.array(16, dtype=np.int64).item()
])
self.assertAllEqual(x, [321, 16])
