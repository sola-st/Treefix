# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/distributed_save_test.py
dataset = dataset_ops.Dataset.range(10)
self.save(dataset)
# TODO(b/250921378) Test loading.
self.assertTrue(
    os.path.exists(os.path.join(self._test_dir, "snapshot.metadata")))
