# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/confusion_matrix_test.py
with self.cached_session():
    dtype = predictions.dtype
    ans = confusion_matrix.confusion_matrix(
        labels, predictions, dtype=dtype, weights=weights,
        num_classes=num_classes).eval()
    self.assertAllClose(truth, ans, atol=1e-10)
    self.assertEqual(ans.dtype, dtype)
