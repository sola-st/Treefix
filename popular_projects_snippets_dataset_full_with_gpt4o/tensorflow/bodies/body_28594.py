# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
num_elements = 10
ds = dataset_ops.Dataset.range(num_elements)
ds = ds.cache()

iterator = iter(ds)
for i in range(num_elements):
    self.assertEqual(next(iterator).numpy(), i)
ckpt = trackable_utils.Checkpoint(iterator=iterator)
manager = checkpoint_management.CheckpointManager(
    ckpt, self.get_temp_dir(), max_to_keep=1)
manager.save()
manager.restore_or_initialize()
with self.assertRaises(StopIteration):
    next(iterator)
