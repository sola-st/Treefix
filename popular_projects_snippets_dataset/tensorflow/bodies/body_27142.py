# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/snapshot_ft_test.py
cluster, _ = self.setup()
write_file(os.path.join(self.source_dir(), bad_split_filename))
with self.assertRaisesRegex(ValueError, "can't parse"):
    cluster.restart_dispatcher()
