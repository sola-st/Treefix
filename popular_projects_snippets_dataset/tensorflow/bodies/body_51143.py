# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
"""Tests that no errors are raised when provided outputs are valid."""
with context.graph_mode():
    loss = {'my_loss': constant_op.constant([0])}
    predictions = {u'output1': constant_op.constant(['foo'])}
    mean, update_op = metrics_module.mean_tensor(constant_op.constant([0]))
    metrics = {
        'metrics': (mean, update_op),
        'metrics2': (constant_op.constant([0]), constant_op.constant([10]))
    }

    outputter = MockSupervisedOutput(loss, predictions, metrics)
    self.assertEqual(outputter.loss['loss/my_loss'], loss['my_loss'])
    self.assertEqual(
        outputter.predictions['predictions/output1'], predictions['output1'])
    self.assertEqual(outputter.metrics['metrics/update_op'].name,
                     'mean/update_op:0')
    self.assertEqual(
        outputter.metrics['metrics2/update_op'], metrics['metrics2'][1])

    # Single Tensor is OK too
    outputter = MockSupervisedOutput(
        loss['my_loss'], predictions['output1'], metrics['metrics'])
    self.assertEqual(outputter.loss, {'loss': loss['my_loss']})
    self.assertEqual(
        outputter.predictions, {'predictions': predictions['output1']})
    self.assertEqual(outputter.metrics['metrics/update_op'].name,
                     'mean/update_op:0')
