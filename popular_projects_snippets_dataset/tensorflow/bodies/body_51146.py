# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
"""Tests that no errors are raised when provided outputs are valid."""
with context.graph_mode():
    loss = {('my', 'loss'): constant_op.constant([0])}
    predictions = {(u'output1', '2'): constant_op.constant(['foo'])}
    mean, update_op = metrics_module.mean_tensor(constant_op.constant([0]))
    metrics = {
        ('metrics', '1'): (mean, update_op),
        ('metrics', '2'): (constant_op.constant([0]),
                           constant_op.constant([10]))
    }

    outputter = MockSupervisedOutput(loss, predictions, metrics)
    self.assertEqual(set(outputter.loss.keys()), set(['loss/my/loss']))
    self.assertEqual(set(outputter.predictions.keys()),
                     set(['predictions/output1/2']))
    self.assertEqual(
        set(outputter.metrics.keys()),
        set([
            'metrics/1/value', 'metrics/1/update_op', 'metrics/2/value',
            'metrics/2/update_op'
        ]))
