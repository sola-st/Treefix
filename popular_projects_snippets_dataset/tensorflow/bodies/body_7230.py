# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
"""Test the device scope of multi-worker MirroredStrategy."""
self._configure_distribution_strategy(distribution)
with distribution.scope():
    a = constant_op.constant(1.)
    with ops.device("/cpu:0"):
        b = constant_op.constant(1.)
    self.assertEqual(a.device, "/job:worker/task:0")
    self.assertEqual(b.device, "/job:worker/task:0/device:CPU:0")
