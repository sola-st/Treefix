# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
"""Tests that a single batched tensor executes together and only once."""
if context.executing_eagerly():
    exit()
with self.cached_session() as sess:
    inp = array_ops.placeholder(dtype=dtypes.int32, shape=[1])
    batched, index, _ = batch_ops.batch(
        [inp], num_batch_threads=1, max_batch_size=2,
        batch_timeout_micros=36000000, grad_timeout_micros=0,
        batching_queue="")
    thread_results = []

    def worker():
        thread_results.extend(
            sess.run([batched, index], feed_dict={inp: [1]}))

    worker_thread = threading.Thread(target=worker)
    worker_thread.start()
    main_results = sess.run([batched, index], feed_dict={inp: [2]})
    worker_thread.join()

    # At this point either the thread or the main did the batch and the other
    # should have empty results.
    if list(thread_results[0][0]):
        batch_t = thread_results[0][0]
        index_t = thread_results[1]
        empty_b = main_results[0][0]
        empty_m = main_results[1]
    else:
        batch_t = main_results[0][0]
        index_t = main_results[1]
        empty_b = thread_results[0][0]
        empty_m = thread_results[1]

    # Check that both the inputs made it out exactly once.
    self.assertAllEqual(sorted(batch_t), (1, 2))
    # Check that we get 2 rows in the index tensor.
    self.assertEqual(len(index_t), 2)
    # Check that the other ones are empty.
    self.assertEqual(len(empty_b), 0)
    self.assertEqual(len(empty_m), 0)
