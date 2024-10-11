# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/snapshot_ft_test.py
cluster, _ = self.setup()
os.makedirs(os.path.join(self.splits_dir(), bad_source_dir_name))
with self.assertRaisesRegex(ValueError, "can't parse"):
    cluster.restart_dispatcher()
