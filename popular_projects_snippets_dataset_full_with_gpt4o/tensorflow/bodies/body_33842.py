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
weights = array_ops.concat(
    [
        constant_op.constant(
            0, shape=[1]), constant_op.constant(
                1, shape=[8]), constant_op.constant(
                    0, shape=[1])
    ],
    0)
with self.cached_session():
    miou, update_op = metrics.mean_iou(
        labels, predictions, num_classes, weights=weights)
    self.evaluate(variables.local_variables_initializer())
    self.assertAllEqual([[2, 0], [2, 4]], update_op)
    desired_miou = np.mean([2. / 4., 4. / 6.])
    self.assertAlmostEqual(desired_miou, self.evaluate(miou))
