# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
dataset_int_scalar = (
    dataset_ops.Dataset.from_tensor_slices([1, 2, 3]).repeat())
dataset_float_vector = (dataset_ops.Dataset.from_tensors([1.0, 2.0, 3.0]))

handle_placeholder = array_ops.placeholder(dtypes.string, shape=[])

feedable_int_scalar = iterator_ops.Iterator.from_string_handle(
    handle_placeholder, dtypes.int32, [])
feedable_int_vector = iterator_ops.Iterator.from_string_handle(
    handle_placeholder, dtypes.int32, [None])
feedable_int_any = iterator_ops.Iterator.from_string_handle(
    handle_placeholder, dtypes.int32)

with self.cached_session() as sess:
    handle_int_scalar = sess.run(dataset_ops.make_one_shot_iterator(
        dataset_int_scalar).string_handle())
    handle_float_vector = sess.run(dataset_ops.make_one_shot_iterator(
        dataset_float_vector).string_handle())

    self.assertEqual(1,
                     sess.run(
                         feedable_int_scalar.get_next(),
                         feed_dict={handle_placeholder: handle_int_scalar}))

    self.assertEqual(2,
                     sess.run(
                         feedable_int_any.get_next(),
                         feed_dict={handle_placeholder: handle_int_scalar}))

    with self.assertRaises(errors.InvalidArgumentError):
        print(sess.run(
            feedable_int_vector.get_next(),
            feed_dict={handle_placeholder: handle_int_scalar}))

    with self.assertRaises(errors.InvalidArgumentError):
        print(sess.run(
            feedable_int_vector.get_next(),
            feed_dict={handle_placeholder: handle_float_vector}))
