# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/snapshot_ft_test.py
cluster, _ = self.setup()
write_file(os.path.join(self.source_dir(), "split_0_1"))
with self.assertRaisesRegex(ValueError, "found missing global"):
    cluster.restart_dispatcher()
