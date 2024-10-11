# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/snapshot_ft_test.py
cluster, _ = self.setup()
os.makedirs(os.path.join(self.splits_dir(), "source_1"))
with self.assertRaisesRegex(ValueError, "found conflict"):
    cluster.restart_dispatcher()
