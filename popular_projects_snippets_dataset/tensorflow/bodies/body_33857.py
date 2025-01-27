# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = array_ops.concat([
    constant_op.constant(0, shape=[5]), constant_op.constant(1, shape=[5])
], 0)
labels = array_ops.concat([
    constant_op.constant(0, shape=[3]), constant_op.constant(1, shape=[7])
], 0)
num_classes = 2
weights = array_ops.concat([
    constant_op.constant(0, shape=[1]), constant_op.constant(1, shape=[8]),
    constant_op.constant(0, shape=[1])
], 0)
with self.cached_session():
    mean_accuracy, update_op = metrics.mean_per_class_accuracy(
        labels, predictions, num_classes, weights=weights)
    self.evaluate(variables.local_variables_initializer())
    desired_accuracy = np.array([2. / 2., 4. / 6.], dtype=np.float32)
    self.assertAllEqual(desired_accuracy, update_op)
    desired_mean_accuracy = np.mean(desired_accuracy)
    self.assertAlmostEqual(desired_mean_accuracy,
                           self.evaluate(mean_accuracy))
