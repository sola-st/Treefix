# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
dataset_3 = dataset_ops.Dataset.from_tensors(
    constant_op.constant([1, 2, 3]))
dataset_4 = dataset_ops.Dataset.from_tensors(
    constant_op.constant([4, 5, 6, 7]))
iterator = iterator_ops.Iterator.from_structure(
    dataset_ops.get_legacy_output_types(dataset_3), [None])

dataset_3_init_op = iterator.make_initializer(dataset_3)
dataset_4_init_op = iterator.make_initializer(dataset_4)
get_next = iterator.get_next()

self.assertEqual(
    dataset_ops.get_legacy_output_types(dataset_3),
    dataset_ops.get_legacy_output_types(iterator))
self.assertEqual(
    dataset_ops.get_legacy_output_types(dataset_4),
    dataset_ops.get_legacy_output_types(iterator))
self.assertEqual(
    [None], dataset_ops.get_legacy_output_shapes(iterator).as_list())

with self.cached_session() as sess:
    # The iterator is initially uninitialized.
    with self.assertRaises(errors.FailedPreconditionError):
        sess.run(get_next)

    # Initialize with one dataset.
    sess.run(dataset_3_init_op)
    self.assertAllEqual([1, 2, 3], sess.run(get_next))
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(get_next)

    # Initialize with a different dataset.
    sess.run(dataset_4_init_op)
    self.assertAllEqual([4, 5, 6, 7], sess.run(get_next))
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(get_next)

    # Reinitialize with the first dataset.
    sess.run(dataset_3_init_op)
    self.assertAllEqual([1, 2, 3], sess.run(get_next))
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(get_next)
