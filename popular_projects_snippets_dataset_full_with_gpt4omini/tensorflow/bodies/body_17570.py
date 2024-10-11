# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_test.py
output = self.evaluate(init(shape))
self.assertEqual(output.shape, shape)
lim = 3e-2
if target_std is not None:
    self.assertGreater(lim, abs(output.std() - target_std))
if target_mean is not None:
    self.assertGreater(lim, abs(output.mean() - target_mean))
if target_max is not None:
    self.assertGreater(lim, abs(output.max() - target_max))
if target_min is not None:
    self.assertGreater(lim, abs(output.min() - target_min))
