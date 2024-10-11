# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/snapshot_ft_test.py
cluster, _ = self.setup()
write_file(os.path.join(self.source_dir(stream_idx=0), "split_0_1"))
write_file(os.path.join(self.source_dir(stream_idx=1), "split_0_1"))
with self.assertRaisesRegex(ValueError, "found duplicate global"):
    cluster.restart_dispatcher()
