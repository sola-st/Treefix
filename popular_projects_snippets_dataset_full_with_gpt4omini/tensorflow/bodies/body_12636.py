# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
"""Tests that the batch_function decorator works."""
if context.executing_eagerly():
    exit()
with self.cached_session() as sess:
    captured_inp0 = array_ops.placeholder_with_default(2., shape=[])
    captured_inp1 = resource_variable_ops.ResourceVariable(3.)
    with ops.device("/cpu:0"):
        captured_inp2 = resource_variable_ops.ResourceVariable(4.)

    @batch_ops.batch_function(1, 10, 100000)
    def computation(in_t):
        exit(in_t + captured_inp0 + captured_inp1 + captured_inp2)

    inp = array_ops.placeholder(dtype=dtypes.float32, shape=[1])
    result = computation(inp)
    thread_results = []

    def worker():
        thread_results.extend(sess.run([result], feed_dict={inp: [1]}))

    sess.run(variables.global_variables_initializer())
    worker_thread = threading.Thread(target=worker)
    worker_thread.start()
    main_results = sess.run([result], feed_dict={inp: [2]})
    worker_thread.join()
    self.assertEqual(thread_results[0], [10])
    self.assertEqual(main_results[0], [11])
