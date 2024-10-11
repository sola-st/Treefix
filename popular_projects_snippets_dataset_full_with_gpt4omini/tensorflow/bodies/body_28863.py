# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
ckpt_dir = self.get_temp_dir()
dataset = dataset_ops.Dataset.range(10)
iterator = iter(dataset)
ckpt = trackable_utils.Checkpoint(iterator=iterator)
manager = checkpoint_management.CheckpointManager(
    ckpt, ckpt_dir, max_to_keep=3)

for _ in range(5):
    next(iterator)
manager.save()

# Define a different dataset and try to restore into its iterator.
dataset = dataset_ops.Dataset.from_tensor_slices([1, 2, 3])
iterator = iter(dataset)
ckpt = trackable_utils.Checkpoint(iterator=iterator)
manager = checkpoint_management.CheckpointManager(
    ckpt, ckpt_dir, max_to_keep=3)
with self.assertRaisesRegex(
    errors.NotFoundError,
    "Make sure the dataset definition has not changed"):
    ckpt.restore(manager.latest_checkpoint)
