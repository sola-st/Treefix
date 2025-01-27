# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session() as sess:
    # First dimension of second component is unknown, second
    # dimension must be 3.
    q = data_flow_ops.PaddingFIFOQueue(10,
                                       (dtypes_lib.int32, dtypes_lib.int32), (
                                           (2, 2), (None, 3)))
    elems_ok = np.array([1] * 8).reshape((2, 2, 2)).astype(np.int32)
    elems_bad = array_ops.placeholder(dtypes_lib.int32)
    enqueue_op = q.enqueue_many((elems_ok, elems_bad))
    dequeued_t = q.dequeue_many(2)
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        "Shape mismatch in tuple component 1. "
        r"Expected \[2,\?,3\], got \[2,3,4\]"):
        sess.run([enqueue_op],
                 feed_dict={elems_bad: np.array([1] * 24).reshape((2, 3, 4))})
        self.evaluate(dequeued_t)
