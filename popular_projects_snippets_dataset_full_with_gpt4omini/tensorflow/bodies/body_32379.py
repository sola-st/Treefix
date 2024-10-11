# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/reconstruction_ops_test.py
signal = array_ops.ones([3, 5])
reconstruction = reconstruction_ops.overlap_and_add(signal, 2)
self.assertEqual(reconstruction.shape.as_list(), [9])
expected_output = np.array([1, 1, 2, 2, 3, 2, 2, 1, 1])
self.assertAllClose(reconstruction, expected_output)
