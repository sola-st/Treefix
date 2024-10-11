# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
scalar = loss_scale_module.FixedLossScale(123)
self.assertIsInstance(scalar(), ops.Tensor)
