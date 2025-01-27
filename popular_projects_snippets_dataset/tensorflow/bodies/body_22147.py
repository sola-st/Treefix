# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/mixed_precision_test.py
opt = gradient_descent_v1.GradientDescentOptimizer(1.0)
opt = mixed_precision.enable_mixed_precision_graph_rewrite_v1(opt, 123.)
self.assertIsInstance(
    opt, loss_scale_optimizer_v1.MixedPrecisionLossScaleOptimizer)
self.assertEqual(self.evaluate(opt._loss_scale()), 123.)
