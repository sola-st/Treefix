# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
dataset = dataset_ops.Dataset.from_tensor_slices([1, 2, 3])
one_shot_iterator = dataset_ops.make_one_shot_iterator(dataset)
initializable_iterator = dataset_ops.make_initializable_iterator(dataset)
structure_iterator = iterator_ops.Iterator.from_structure(
    dataset_ops.get_legacy_output_types(dataset))

created_ops = len(ops.get_default_graph().get_operations())

self.assertIs(one_shot_iterator.string_handle(),
              one_shot_iterator.string_handle())
self.assertIs(initializable_iterator.string_handle(),
              initializable_iterator.string_handle())
self.assertIs(structure_iterator.string_handle(),
              structure_iterator.string_handle())

# Assert that getting the (default) string handle creates no ops.
self.assertLen(ops.get_default_graph().get_operations(), created_ops)

# Specifying an explicit name will create a new op.
handle_with_name = one_shot_iterator.string_handle(name="foo")
self.assertEqual("foo", handle_with_name.op.name)
self.assertIsNot(one_shot_iterator.string_handle(), handle_with_name)

handle_with_same_name = one_shot_iterator.string_handle(name="foo")
self.assertEqual("foo_1", handle_with_same_name.op.name)
self.assertIsNot(handle_with_name, handle_with_same_name)
