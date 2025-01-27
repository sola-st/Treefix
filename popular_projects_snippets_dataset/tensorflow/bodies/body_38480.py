# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/confusion_matrix_test.py
labels = np.asarray([1, 2])
predictions = np.asarray([1, 2, 3])
self.assertRaisesRegex(ValueError, "must be equal",
                       confusion_matrix.confusion_matrix, predictions,
                       labels)
