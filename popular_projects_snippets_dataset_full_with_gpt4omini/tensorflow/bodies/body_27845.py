# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
# Batches of size 512M
dataset = dataset_ops.Dataset.from_tensors(
    array_ops.ones((64, 1024, 1024), dtype=dtypes.float32)).repeat()
dataset = dataset.batch(2, num_parallel_calls=5)
iterator = iter(dataset)
next(iterator)  # request an element to fill the buffer
ckpt = trackable_utils.Checkpoint(iterator=iterator)
manager = checkpoint_management.CheckpointManager(
    ckpt, self.get_temp_dir(), max_to_keep=1)
manager.save()
