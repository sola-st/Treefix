# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = array_ops.zeros([40])
labels = array_ops.ones([40])
num_classes = 2
with self.cached_session():
    mean_accuracy, update_op = metrics.mean_per_class_accuracy(
        labels, predictions, num_classes)
    self.evaluate(variables.local_variables_initializer())
    self.assertAllEqual([0.0, 0.0], update_op)
    self.assertEqual(0., self.evaluate(mean_accuracy))
