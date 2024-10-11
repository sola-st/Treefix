# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
# Tensor of size 512M
dataset = dataset_ops.Dataset.from_tensors(
    array_ops.ones((128, 1024, 1024), dtype=dtypes.float32))
dataset = dataset.repeat()
# Set parallelism to 5 to exceed the 2GB protobuf limit
dataset = dataset.map(lambda x: x * 2, num_parallel_calls=5)
iterator = iter(dataset)
next(iterator)  # request an element to fill the parallel map buffer
ckpt = trackable_utils.Checkpoint(iterator=iterator)
manager = checkpoint_management.CheckpointManager(
    ckpt, self.get_temp_dir(), max_to_keep=1)
manager.save()
