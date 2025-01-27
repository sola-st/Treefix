# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
dataset = dataset_ops.Dataset.from_tensor_slices([1, 2, 3, 4, 5, 6]).map(
    math_ops.square).batch(2)
iterator = iter(dataset)
get_next = iterator.get_next
checkpoint = trackable_utils.Checkpoint(iterator=iterator)
self.assertAllEqual([1, 4], get_next())
save_path = checkpoint.save(checkpoint_prefix)
self.assertAllEqual([9, 16], get_next())
self.assertAllEqual([25, 36], get_next())
checkpoint.restore(save_path).run_restore_ops()
self.assertAllEqual([9, 16], get_next())
self.assertAllEqual([25, 36], get_next())
with self.assertRaises(errors.OutOfRangeError):
    get_next()
