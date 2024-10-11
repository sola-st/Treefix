# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
predictions = array_ops.zeros([40])
labels = array_ops.ones([40])
num_classes = 2
with self.cached_session():
    miou, update_op = metrics.mean_iou(labels, predictions, num_classes)
    self.evaluate(variables.local_variables_initializer())
    self.assertAllEqual([[0, 0], [40, 0]], update_op)
    self.assertEqual(0., self.evaluate(miou))
