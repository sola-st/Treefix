# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer_test.py
opt = gradient_descent.GradientDescentOptimizer(1.0)
with self.assertRaisesRegex(ValueError, r'loss_scale cannot be None'):
    loss_scale_optimizer.MixedPrecisionLossScaleOptimizer(opt, None)
