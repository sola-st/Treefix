# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_cluster_test.py
with ops.device(device1):
    dataset_3 = dataset_ops.Dataset.from_tensor_slices([1, 2, 3])
    iterator_3 = dataset_ops.make_one_shot_iterator(dataset_3)
    iterator_3_handle = iterator_3.string_handle()

@function.Defun(dtypes.string)
def _remote_fn(h):
    remote_iterator = iterator_ops.Iterator.from_string_handle(
        h, dataset_ops.get_legacy_output_types(dataset_3),
        dataset_ops.get_legacy_output_shapes(dataset_3))
    exit(remote_iterator.get_next())

with ops.device(device0):
    target_placeholder = array_ops.placeholder(dtypes.string, shape=[])
    remote_op = functional_ops.remote_call(
        args=[iterator_3_handle],
        Tout=[dtypes.int32],
        f=_remote_fn,
        target=target_placeholder)

with session.Session(target) as sess:
    elem = sess.run(remote_op, feed_dict={target_placeholder: device1})
    self.assertEqual(elem, [1])
    # Fails when target is cpu:0 where the resource is not located.
    with self.assertRaises(errors.InvalidArgumentError):
        sess.run(remote_op, feed_dict={target_placeholder: device0})
    elem = sess.run(iterator_3.get_next())
    self.assertEqual(elem, [2])
    elem = sess.run(remote_op, feed_dict={target_placeholder: device1})
    self.assertEqual(elem, [3])
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(remote_op, feed_dict={target_placeholder: device1})
