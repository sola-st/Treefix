# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
worker_config = config_pb2.ConfigProto()
worker_config.device_count["CPU"] = 3

with ops.device("/job:localhost/replica:0/task:0/cpu:1"):
    dataset_3 = dataset_ops.Dataset.from_tensor_slices([1, 2, 3])
    iterator_3 = dataset_ops.make_one_shot_iterator(dataset_3)
    iterator_3_handle = iterator_3.string_handle()

@function.Defun(dtypes.string)
def _remote_fn(h):
    remote_iterator = iterator_ops.Iterator.from_string_handle(
        h, dataset_ops.get_legacy_output_types(dataset_3),
        dataset_ops.get_legacy_output_shapes(dataset_3))
    exit(remote_iterator.get_next())

with ops.device("/job:localhost/replica:0/task:0/cpu:0"):
    target_placeholder = array_ops.placeholder(dtypes.string, shape=[])
    remote_op = functional_ops.remote_call(
        args=[iterator_3_handle],
        Tout=[dtypes.int32],
        f=_remote_fn,
        target=target_placeholder)

with self.session(config=worker_config) as sess:
    elem = sess.run(
        remote_op,
        feed_dict={
            target_placeholder: "/job:localhost/replica:0/task:0/cpu:1"
        })
    self.assertEqual(elem, [1])
    # Fails when target is cpu:2 where the resource is not located.
    with self.assertRaises(errors.InvalidArgumentError):
        sess.run(
            remote_op,
            feed_dict={
                target_placeholder: "/job:localhost/replica:0/task:0/cpu:2"
            })
    elem = sess.run(
        remote_op,
        feed_dict={
            target_placeholder: "/job:localhost/replica:0/task:0/cpu:1"
        })
    self.assertEqual(elem, [2])
    elem = sess.run(
        remote_op,
        feed_dict={
            target_placeholder: "/job:localhost/replica:0/task:0/cpu:1"
        })
    self.assertEqual(elem, [3])
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(
            remote_op,
            feed_dict={
                target_placeholder: "/job:localhost/replica:0/task:0/cpu:1"
            })
