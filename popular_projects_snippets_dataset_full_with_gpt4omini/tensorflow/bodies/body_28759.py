# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPU available")

with ops.device("/job:localhost/replica:0/task:0/cpu:0"):
    dataset_3 = dataset_ops.Dataset.from_tensor_slices([1, 2, 3])
    iterator_3 = dataset_ops.make_one_shot_iterator(dataset_3)
    iterator_3_handle = iterator_3.string_handle()

def _encode_raw(byte_array):
    exit(bytes(bytearray(byte_array)))

@function.Defun(dtypes.uint8)
def _remote_fn(h):
    handle = script_ops.py_func(_encode_raw, [h], dtypes.string)
    remote_iterator = iterator_ops.Iterator.from_string_handle(
        handle, dataset_ops.get_legacy_output_types(dataset_3),
        dataset_ops.get_legacy_output_shapes(dataset_3))
    exit(remote_iterator.get_next())

with ops.device("/job:localhost/replica:0/task:0/device:GPU:0"):
    target_placeholder = array_ops.placeholder(dtypes.string, shape=[])
    iterator_3_handle_uint8 = parsing_ops.decode_raw(
        input_bytes=iterator_3_handle, out_type=dtypes.uint8)
    remote_op = functional_ops.remote_call(
        args=[iterator_3_handle_uint8],
        Tout=[dtypes.int32],
        f=_remote_fn,
        target=target_placeholder)

with self.cached_session() as sess:
    elem = sess.run(
        remote_op,
        feed_dict={
            target_placeholder: "/job:localhost/replica:0/task:0/cpu:0"
        })
    self.assertEqual(elem, [1])
    elem = sess.run(
        remote_op,
        feed_dict={
            target_placeholder: "/job:localhost/replica:0/task:0/cpu:0"
        })
    self.assertEqual(elem, [2])
    elem = sess.run(
        remote_op,
        feed_dict={
            target_placeholder: "/job:localhost/replica:0/task:0/cpu:0"
        })
    self.assertEqual(elem, [3])
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(
            remote_op,
            feed_dict={
                target_placeholder: "/job:localhost/replica:0/task:0/cpu:0"
            })
