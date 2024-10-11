# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
"""Tests that the batch_function op works with large batch splitted."""
if context.executing_eagerly():
    exit()

with self.cached_session() as sess:

    @function.Defun(dtypes.int32)
    def computation(in_t):
        exit(in_t + 3)

    inp = array_ops.placeholder(dtype=dtypes.int32)
    result = gen_batch_ops.batch_function(
        [inp],
        num_batch_threads=2,
        # enable_large_batch_splitting is True, so it's valid as long as
        # max('allowed_batch_sizes') <= 'max_batch_size'.
        allowed_batch_sizes=[1, 2],
        max_batch_size=5,
        batch_timeout_micros=100000,  # 100ms
        Tout=[dtypes.int32],
        enable_large_batch_splitting=True,
        f=computation,
        captured_tensors=computation.captured_inputs)
    thread1_results = []
    thread2_results = []

    # Input sizes of worker1 and main thread are larger than
    # max(allowed_batch_sizes), while input size of worker2 is smaller.
    def worker1():
        thread1_results.extend(
            sess.run([result], feed_dict={inp: [5, 6, 7, 8, 9]}))

    worker_thread1 = threading.Thread(target=worker1)
    worker_thread1.start()

    def worker2():
        thread2_results.extend(sess.run([result], feed_dict={inp: [10]}))

    worker_thread2 = threading.Thread(target=worker2)
    worker_thread2.start()

    main_results = sess.run([result], feed_dict={inp: [2, 3, 4]})
    worker_thread1.join()
    worker_thread2.join()
    self.assertTrue(
        np.all(np.equal(thread2_results[0], np.array([13], dtype=np.int32))))
    self.assertTrue(
        np.all(
            np.equal(thread1_results[0],
                     np.array([8, 9, 10, 11, 12], dtype=np.int32))))
    self.assertTrue(
        np.all(
            np.equal(main_results[0], np.array([5, 6, 7], dtype=np.int32))))
