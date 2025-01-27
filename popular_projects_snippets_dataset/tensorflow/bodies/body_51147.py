# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
"""Tests that no errors are raised when provided outputs are valid."""
with context.graph_mode():
    loss = {'loss': constant_op.constant([0])}
    predictions = {u'predictions': constant_op.constant(['foo'])}
    mean, update_op = metrics_module.mean_tensor(constant_op.constant([0]))
    metrics = {
        'metrics_1': (mean, update_op),
        'metrics_2': (constant_op.constant([0]), constant_op.constant([10]))
    }

    outputter = MockSupervisedOutput(loss, predictions, metrics)
    self.assertEqual(set(outputter.loss.keys()), set(['loss']))
    self.assertEqual(set(outputter.predictions.keys()), set(['predictions']))
    self.assertEqual(
        set(outputter.metrics.keys()),
        set([
            'metrics_1/value', 'metrics_1/update_op', 'metrics_2/update_op',
            'metrics_2/value'
        ]))
