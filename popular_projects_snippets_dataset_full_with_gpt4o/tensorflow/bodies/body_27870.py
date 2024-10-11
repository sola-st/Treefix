# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/io_test.py
dataset = dataset_ops.Dataset.range(42)
dataset.save(self._save_dir)
verify_fn(self, self._build_ds, num_outputs=42)
