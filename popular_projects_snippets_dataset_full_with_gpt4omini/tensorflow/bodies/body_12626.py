# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
"""Tests that multiple batched tensors execute together."""
if context.executing_eagerly():
    exit()
with self.cached_session() as sess:
    inp0 = array_ops.placeholder(dtype=dtypes.int32, shape=[1])
    inp1 = array_ops.placeholder(dtype=dtypes.int32, shape=[1])
    batched, _, _ = batch_ops.batch(
        [inp0, inp1],
        num_batch_threads=1,
        max_batch_size=2,
        batch_timeout_micros=36000000,
        grad_timeout_micros=0,
        batching_queue="")
    thread_results = []

    def worker():
        thread_results.extend(
            sess.run([batched], feed_dict={inp0: [1],
                                           inp1: [2]}))

    worker_thread = threading.Thread(target=worker)
    worker_thread.start()
    main_results = sess.run([batched], feed_dict={inp0: [2], inp1: [3]})
    worker_thread.join()

    # At this point either the thread or the main did the batch and the other
    # should have empty results.
    if list(thread_results[0][0]):
        batch_t = thread_results[0]
        empty_t = main_results[0]
    else:
        batch_t = main_results[0]
        empty_t = thread_results[0]

    # Assert that the tensors were batched together.
    self.assertAllEqual(sorted(batch_t[0]), [1, 2])
    self.assertAllEqual(sorted(batch_t[1]), [2, 3])
    self.assertAllEqual(empty_t[0], [])
    self.assertAllEqual(empty_t[1], [])
