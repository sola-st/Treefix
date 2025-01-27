# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = array_ops.zeros([40])
labels = array_ops.zeros([40])
num_classes = 1
with self.cached_session():
    mean_accuracy, update_op = metrics.mean_per_class_accuracy(
        labels, predictions, num_classes)
    self.evaluate(variables.local_variables_initializer())
    self.assertEqual(1.0, self.evaluate(update_op)[0])
    self.assertEqual(1.0, self.evaluate(mean_accuracy))
