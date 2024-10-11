# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
with context.graph_mode():
    loss = {'my_loss': constant_op.constant([0])}
    predictions = {u'output1': constant_op.constant(['foo'])}
    mean, update_op = metrics_module.mean_tensor(constant_op.constant([0]))
    metrics = {
        'metrics_1': (mean, update_op),
        'metrics_2': (constant_op.constant([0]), constant_op.constant([10]))
    }

    outputter = export_output_lib.TrainOutput(loss, predictions, metrics)

    receiver = {u'features': constant_op.constant(100, shape=(100, 2)),
                'labels': constant_op.constant(100, shape=(100, 1))}
    sig_def = outputter.as_signature_def(receiver)

    self.assertIn('loss/my_loss', sig_def.outputs)
    self.assertIn('metrics_1/value', sig_def.outputs)
    self.assertIn('metrics_2/value', sig_def.outputs)
    self.assertIn('predictions/output1', sig_def.outputs)
    self.assertIn('features', sig_def.inputs)
