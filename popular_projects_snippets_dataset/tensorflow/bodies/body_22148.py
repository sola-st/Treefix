# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/mixed_precision_test.py
opt = 1
expected_regex = ('"opt" must be an instance of a tf.train.Optimizer or '
                  'a tf.keras.optimizers.Optimizer, but got')
with self.assertRaisesRegex(ValueError, expected_regex):
    mixed_precision.enable_mixed_precision_graph_rewrite_v1(opt)
self.assertFalse(config.get_optimizer_experimental_options()
                 .get('auto_mixed_precision', False))

opt = gradient_descent_v1.GradientDescentOptimizer(1.0)
opt = loss_scale_optimizer_v1.MixedPrecisionLossScaleOptimizer(opt,
                                                               'dynamic')
with self.assertRaisesRegex(
    ValueError, '"opt" must not already be an instance of a '
    'MixedPrecisionLossScaleOptimizer.'):
    mixed_precision.enable_mixed_precision_graph_rewrite_v1(opt)
self.assertFalse(config.get_optimizer_experimental_options()
                 .get('auto_mixed_precision', False))
