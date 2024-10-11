# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/confusion_matrix_test.py
labels = np.asarray([1, 1, 0, 3, 5], dtype=np.int32)
predictions = np.asarray([2, 1, 0, 2, 2], dtype=np.int32)
with self.assertRaisesWithPredicateMatch(errors_impl.InvalidArgumentError,
                                         "`labels`.*out of bound"):
    self._testConfMatrix(
        labels=labels, predictions=predictions, num_classes=3, truth=None)
