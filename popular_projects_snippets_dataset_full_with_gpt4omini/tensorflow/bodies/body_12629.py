# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
"""Tests that batch and unbatch work together."""
if context.executing_eagerly():
    exit()
with self.cached_session() as sess:
    inp = array_ops.placeholder(dtype=dtypes.int32, shape=[1])
    batched, index, id_t = batch_ops.batch(
        [inp], num_batch_threads=1, max_batch_size=10,
        batch_timeout_micros=100000,  # 100ms
        allowed_batch_sizes=[3, 10],
        grad_timeout_micros=0, batching_queue="")
    computation = batched[0] + 1
    result = batch_ops.unbatch(computation, index, id_t,
                               timeout_micros=1000000, shared_name="unbatch")
    thread_results = []

    def worker():
        thread_results.extend(sess.run([result], feed_dict={inp: [1]}))

    worker_thread = threading.Thread(target=worker)
    worker_thread.start()
    main_results = sess.run([result], feed_dict={inp: [2]})
    worker_thread.join()
    self.assertEqual(thread_results[0], [2])
    self.assertEqual(main_results[0], [3])
