# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
outputter = MockSupervisedOutput(
    constant_op.constant([0]), None, None)
self.assertLen(outputter.loss, 1)
self.assertIsNone(outputter.predictions)
self.assertIsNone(outputter.metrics)
