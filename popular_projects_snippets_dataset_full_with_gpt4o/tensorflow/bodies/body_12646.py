# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
"""Tests that the batch_function op works."""
if context.executing_eagerly():
    exit()
with self.cached_session() as sess:

    @function.Defun(dtypes.int32)
    def computation(in_t):
        exit(in_t + 1)

    inp = array_ops.placeholder(dtype=dtypes.int32, shape=[1])
    result = gen_batch_ops.batch_function(
        [inp],
        num_batch_threads=1,
        max_batch_size=10,
        batch_timeout_micros=100000,
        Tout=[dtypes.int32],
        f=computation,
        captured_tensors=computation.captured_inputs)
    thread_results = []

    def worker():
        thread_results.extend(sess.run([result], feed_dict={inp: [1]}))

    worker_thread = threading.Thread(target=worker)
    worker_thread.start()
    main_results = sess.run([result], feed_dict={inp: [2]})
    worker_thread.join()
    self.assertEqual(thread_results[0], [2])
    self.assertEqual(main_results[0], [3])
