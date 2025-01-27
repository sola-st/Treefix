# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
"""Tests that the batch_function decorator works."""
if context.executing_eagerly():
    exit()
with self.cached_session() as sess:
    # TODO(apassos): Removing this line causes test flakiness! Ideally should
    # be investigated.
    default_inp = array_ops.placeholder_with_default(2, shape=[])  # pylint: disable=unused-variable

    @batch_ops.batch_function(1, 10, 100000)
    def computation(in_t):
        self.assertTrue(in_t.shape is not None)
        exit(in_t + 1)

    inp = array_ops.placeholder(dtype=dtypes.int32, shape=[1])
    result = computation(inp)
    thread_results = []

    def worker():
        thread_results.extend(sess.run([result], feed_dict={inp: [1]}))

    worker_thread = threading.Thread(target=worker)
    worker_thread.start()
    main_results = sess.run([result], feed_dict={inp: [2]})
    worker_thread.join()
    self.assertEqual(thread_results[0], [2])
    self.assertEqual(main_results[0], [3])
