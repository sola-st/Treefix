# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
dataset = dataset_ops.Dataset.from_tensor_slices(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
dataset = dataset.map(math_ops.square).batch(2)
iterator_1 = iter(dataset)
get_next_1 = iterator_1.get_next
iterator_2 = iter(dataset)
get_next_2 = iterator_2.get_next
dataset_2 = dataset_ops.Dataset.range(10)
iterator_3 = iter(dataset_2)
get_next_3 = iterator_3.get_next
checkpoint = trackable_utils.Checkpoint(
    iterator_1=iterator_1, iterator_2=iterator_2, iterator_3=iterator_3)
self.assertAllEqual([1, 4], get_next_1())
self.assertAllEqual(0, get_next_3())
self.assertAllEqual(1, get_next_3())
self.assertAllEqual(2, get_next_3())
save_path = checkpoint.save(checkpoint_prefix)
self.assertAllEqual([1, 4], get_next_2())
self.assertAllEqual([9, 16], get_next_2())
self.assertAllEqual(3, get_next_3())
checkpoint.restore(save_path).run_restore_ops()
self.assertAllEqual([9, 16], get_next_1())
self.assertAllEqual([1, 4], get_next_2())
self.assertAllEqual(3, get_next_3())
