# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
dataset_3 = dataset_ops.Dataset.from_tensor_slices([1, 2, 3])
dataset_4 = dataset_ops.Dataset.from_tensor_slices([10, 20, 30, 40])

iterator_3 = dataset_ops.make_one_shot_iterator(dataset_3)
iterator_4 = dataset_ops.make_one_shot_iterator(dataset_4)

handle_placeholder = array_ops.placeholder(dtypes.string, shape=[])
feedable_iterator = iterator_ops.Iterator.from_string_handle(
    handle_placeholder, dataset_ops.get_legacy_output_types(dataset_3),
    dataset_ops.get_legacy_output_shapes(dataset_3))
next_element = feedable_iterator.get_next()

self.assertTrue(
    structure.are_compatible(
        dataset_ops.get_structure(dataset_3),
        dataset_ops.get_structure(feedable_iterator)))

with self.cached_session() as sess:
    iterator_3_handle = sess.run(iterator_3.string_handle())
    iterator_4_handle = sess.run(iterator_4.string_handle())

    self.assertEqual(10,
                     sess.run(
                         next_element,
                         feed_dict={handle_placeholder: iterator_4_handle}))
    self.assertEqual(1,
                     sess.run(
                         next_element,
                         feed_dict={handle_placeholder: iterator_3_handle}))
    self.assertEqual(20,
                     sess.run(
                         next_element,
                         feed_dict={handle_placeholder: iterator_4_handle}))
    self.assertEqual(2,
                     sess.run(
                         next_element,
                         feed_dict={handle_placeholder: iterator_3_handle}))
    self.assertEqual(30,
                     sess.run(
                         next_element,
                         feed_dict={handle_placeholder: iterator_4_handle}))
    self.assertEqual(3,
                     sess.run(
                         next_element,
                         feed_dict={handle_placeholder: iterator_3_handle}))
    self.assertEqual(40,
                     sess.run(
                         next_element,
                         feed_dict={handle_placeholder: iterator_4_handle}))
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(
            next_element, feed_dict={handle_placeholder: iterator_3_handle})
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(
            next_element, feed_dict={handle_placeholder: iterator_4_handle})
