# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
dataset = dataset_ops.Dataset.range(3)
iterator = iter(dataset)
get_next = iterator.get_next
checkpoint = trackable_utils.Checkpoint(iterator=iterator)
self.assertAllEqual(0, get_next())
self.assertAllEqual(1, get_next())
save_path = checkpoint.save(checkpoint_prefix)
self.assertAllEqual(2, get_next())
checkpoint.restore(save_path).run_restore_ops()
self.assertAllEqual(2, get_next())
save_path = checkpoint.save(checkpoint_prefix)
checkpoint.restore(save_path).run_restore_ops()
with self.assertRaises(errors.OutOfRangeError):
    get_next()
