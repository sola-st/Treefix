# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/broadcast_to_ops_test.py
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "110,53,104,147,157,123,5,24,188,40,5,2"):
    output_shape = [110, 53, 104, 147, 157, 123, 5, 24, 188, 40, 5, 2]
    x = np.array([1, 2, 3], dtype=np.int32)
    v = array_ops.broadcast_to(constant_op.constant(x), output_shape)
    self.evaluate(v)
