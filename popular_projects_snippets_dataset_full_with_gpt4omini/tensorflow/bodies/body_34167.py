# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/priority_queue_test.py
with self.cached_session() as sess:
    input_priority = array_ops.placeholder(dtypes.int64)
    input_other = array_ops.placeholder(dtypes.string)
    q = data_flow_ops.PriorityQueue(2000, (dtypes.string,), (()))

    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        r"Shape mismatch in tuple component 0. Expected \[\], got \[2\]"):
        sess.run([q.enqueue((input_priority, input_other))],
                 feed_dict={
                     input_priority: np.array(
                         [0, 2], dtype=np.int64),
                     input_other: np.random.rand(3, 5).astype(bytes)
                 })

    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        r"Shape mismatch in tuple component 0. Expected \[2\], got \[2,2\]"):
        sess.run(
            [q.enqueue_many((input_priority, input_other))],
            feed_dict={
                input_priority: np.array(
                    [[0, 2], [3, 4]], dtype=np.int64),
                input_other: np.random.rand(2, 3).astype(bytes)
            })
