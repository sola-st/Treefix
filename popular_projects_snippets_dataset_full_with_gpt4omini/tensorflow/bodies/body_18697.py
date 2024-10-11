# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
if test_util.is_xla_enabled():
    self.skipTest(
        "XLA ignores seeds for RandomNormal, skip xla-enabled test.")
init = init_ops_v2.RandomNormal(0, 7, seed=1)
self._partition_test(init)
