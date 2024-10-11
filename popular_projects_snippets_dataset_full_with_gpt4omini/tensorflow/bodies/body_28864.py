# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
iterator = iter(dataset)
ckpt = trackable_utils.Checkpoint(
    step=variables.Variable(0), iterator=iterator)
manager = checkpoint_management.CheckpointManager(
    ckpt, self.get_temp_dir(), max_to_keep=3)
with self.assertRaises(errors.FailedPreconditionError):
    manager.save()
