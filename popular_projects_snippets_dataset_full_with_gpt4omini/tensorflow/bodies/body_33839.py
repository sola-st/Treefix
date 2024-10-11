# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = array_ops.concat(
    [
        constant_op.constant(
            0, shape=[5]), constant_op.constant(
                1, shape=[5])
    ],
    0)
labels = array_ops.concat(
    [
        constant_op.constant(
            0, shape=[3]), constant_op.constant(
                1, shape=[7])
    ],
    0)
num_classes = 2
with self.cached_session():
    miou, update_op = metrics.mean_iou(labels, predictions, num_classes)
    self.evaluate(variables.local_variables_initializer())
    confusion_matrix = self.evaluate(update_op)
    self.assertAllEqual([[3, 0], [2, 5]], confusion_matrix)
    desired_miou = np.mean([3. / 5., 5. / 7.])
    self.assertAlmostEqual(desired_miou, self.evaluate(miou))
