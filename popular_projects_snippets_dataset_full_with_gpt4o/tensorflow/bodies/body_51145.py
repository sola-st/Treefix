# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
with self.assertRaisesRegex(ValueError, 'predictions output value must'):
    MockSupervisedOutput(constant_op.constant([0]), [3], None)
with self.assertRaisesRegex(ValueError, 'loss output value must'):
    MockSupervisedOutput('str', None, None)
with self.assertRaisesRegex(ValueError, 'metrics output value must'):
    MockSupervisedOutput(None, None, (15.3, 4))
with self.assertRaisesRegex(ValueError, 'loss output key must'):
    MockSupervisedOutput({25: 'Tensor'}, None, None)
