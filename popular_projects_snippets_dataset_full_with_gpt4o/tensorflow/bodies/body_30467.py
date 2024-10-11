# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/fingerprint_op_test.py
data = np.arange(10)
data = np.expand_dims(data, axis=0)
fingerprint0 = self.evaluate(array_ops.fingerprint(data))
fingerprint1 = self.evaluate(array_ops.fingerprint(data[:, 1:]))
self.assertEqual(fingerprint0.ndim, 2)
self.assertTupleEqual(fingerprint0.shape, fingerprint1.shape)
self.assertTrue(np.any(fingerprint0 != fingerprint1))
