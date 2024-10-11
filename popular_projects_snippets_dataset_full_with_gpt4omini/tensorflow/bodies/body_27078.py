# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/distributed_save_test.py
dataset = dataset_ops.Dataset.range(10)
with self.assertRaisesRegex(ValueError, "must be a string"):
    distributed_save_op.distributed_save(dataset, "", 1)
with self.assertRaisesRegex(ValueError, "must not be empty"):
    distributed_save_op.distributed_save(dataset, "", "")
