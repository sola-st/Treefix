# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
for np_type, dtype in [(np.int32, dtypes.int32), (np.half, dtypes.half),
                       (np.float32, dtypes.float32)]:
    x = ops.convert_to_tensor(
        [np.array(65, dtype=np_type),
         np.array(16, dtype=np_type)])
    self.assertEqual(x.dtype, dtype)
    self.assertAllEqual(x, [65, 16])
