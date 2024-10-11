# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
with context.graph_mode():
    loss = {'my_loss': constant_op.constant([0])}
    predictions = {u'output1': constant_op.constant(['foo'])}

    outputter = export_output_lib.EvalOutput(loss, predictions, None)

    receiver = {u'features': constant_op.constant(100, shape=(100, 2)),
                'labels': constant_op.constant(100, shape=(100, 1))}
    sig_def = outputter.as_signature_def(receiver)

    self.assertIn('loss/my_loss', sig_def.outputs)
    self.assertNotIn('metrics/value', sig_def.outputs)
    self.assertIn('predictions/output1', sig_def.outputs)
    self.assertIn('features', sig_def.inputs)
