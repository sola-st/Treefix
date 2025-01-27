# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
if pywrap_sanitizers.is_tsan_enabled():
    self.skipTest("Creating a large buffer causes OOM when using tsan.")
# Batches of size 512M
dataset = dataset_ops.Dataset.from_tensors(
    array_ops.ones((64, 1024, 1024), dtype=dtypes.float32)).repeat()
dataset = dataset.map(lambda x: x+1, num_parallel_calls=5)
dataset = dataset.batch(2)
iterator = iter(dataset)
next(iterator)  # request an element to fill the buffer
ckpt = trackable_utils.Checkpoint(iterator=iterator)
manager = checkpoint_management.CheckpointManager(
    ckpt, self.get_temp_dir(), max_to_keep=1)
manager.save()
