# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
labels = constant_op.constant([
    [[0, 0, 1, 1, 0, 0],
     [1, 0, 0, 0, 0, 1]],
    [[1, 1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0]]])
predictions = constant_op.constant([
    [[0, 0, 2, 1, 1, 0],
     [0, 1, 2, 2, 0, 1]],
    [[0, 0, 2, 1, 1, 1],
     [1, 1, 2, 0, 0, 0]]])
num_classes = 3
with self.cached_session():
    miou, update_op = metrics.mean_iou(labels, predictions, num_classes)
    self.evaluate(variables.local_variables_initializer())
    self.assertAllEqual([[7, 4, 3], [3, 5, 2], [0, 0, 0]], update_op)
    self.assertAlmostEqual(
        1 / 3 * (7 / (7 + 3 + 7) + 5 / (5 + 4 + 5) + 0 / (0 + 5 + 0)),
        self.evaluate(miou))
