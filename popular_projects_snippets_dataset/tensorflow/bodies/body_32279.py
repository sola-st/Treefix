# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/shape_ops_test.py
tensor = constant_op.constant(np.arange(9152), dtypes.int32)
tensor = array_ops.expand_dims(tensor, 0)

result = shape_ops.frame(tensor, 512, 180, pad_end=False)

expected = np.tile(np.arange(512), (49, 1))
expected += np.tile(np.arange(49) * 180, (512, 1)).T

expected = np.expand_dims(expected, axis=0)
expected = np.array(expected, dtype=np.int32)
self.assertAllEqual(expected, result)
