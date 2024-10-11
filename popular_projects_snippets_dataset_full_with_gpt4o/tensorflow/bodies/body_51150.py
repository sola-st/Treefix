# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
"""Tests that ops.Operation is wrapped by a tensor for metric_ops."""
with context.graph_mode():
    loss = {'my_loss': constant_op.constant([0])}
    predictions = {u'output1': constant_op.constant(['foo'])}
    mean, update_op = metrics_module.mean_tensor(constant_op.constant([0]))
    metrics = {
        'metrics_1': (mean, update_op),
        'metrics_2': (constant_op.constant([0]), control_flow_ops.no_op()),
        # Keras metric's update_state() could return a Variable, rather than
        # an Operation or Tensor.
        'keras_1': (constant_op.constant([0.5]),
                    variables.Variable(1.0, name='AssignAddVariableOp_3'))
    }

    outputter = MockSupervisedOutput(loss, predictions, metrics)
    # If we get there, it means constructor succeeded; which is sufficient
    # for testing the constructor.

    self.assertTrue(outputter.metrics['metrics_1/update_op'].name.startswith(
        'mean/update_op'))
    self.assertIsInstance(
        outputter.metrics['metrics_1/update_op'], ops.Tensor)
    self.assertIsInstance(outputter.metrics['metrics_1/value'], ops.Tensor)

    self.assertEqual(outputter.metrics['metrics_2/value'],
                     metrics['metrics_2'][0])
    self.assertTrue(outputter.metrics['metrics_2/update_op'].name.startswith(
        'metric_op_wrapper'))
    self.assertIsInstance(
        outputter.metrics['metrics_2/update_op'], ops.Tensor)
