# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
"""Test that batching with padding up to an allowed batch size works."""
if context.executing_eagerly():
    exit()
with self.cached_session() as sess:
    inp = array_ops.placeholder(dtype=dtypes.int32, shape=[2])
    batched, index, _ = batch_ops.batch(
        [inp], num_batch_threads=1, max_batch_size=10,
        batch_timeout_micros=100000,  # 100ms
        allowed_batch_sizes=[5, 10],
        grad_timeout_micros=0, batching_queue="")
    thread_results = []

    def worker():
        thread_results.extend(
            sess.run([batched, index], feed_dict={inp: [1, 3]}))

    worker_thread = threading.Thread(target=worker)
    worker_thread.start()
    main_results = sess.run([batched, index], feed_dict={inp: [2, 4]})
    worker_thread.join()

    # At this point either the thread or the main did the batch and the other
    # should have empty results.
    if list(thread_results[0][0]):
        batch_t = thread_results[0][0]
    else:
        batch_t = main_results[0][0]

    # Check that the batch tensor incorporates the padding.
    self.assertEqual(len(batch_t), 5)
