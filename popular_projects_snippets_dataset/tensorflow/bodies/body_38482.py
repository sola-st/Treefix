# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/confusion_matrix_test.py
labels = np.arange(2)
predictions = np.arange(2)
with self.cached_session():
    cm = confusion_matrix.confusion_matrix(
        labels, predictions, dtype=dtypes.int64)
    tf_cm = self.evaluate(cm)
self.assertEqual(tf_cm.dtype, np.int64)
