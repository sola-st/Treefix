# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/confusion_matrix_test.py
"""This is a test of the example provided in pydoc."""
with self.cached_session():
    self.assertAllEqual([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1]
    ], self.evaluate(confusion_matrix.confusion_matrix(
        labels=[1, 2, 4], predictions=[2, 2, 4])))
