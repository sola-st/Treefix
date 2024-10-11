# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
if context.executing_eagerly():
    exit()
with self.cached_session() as sess:

    @batch_ops.batch_function(1, 10, 100000)
    def computation(in_t):
        # index is 0 on CPU and 1 on GPU
        index = gen_functional_ops.DeviceIndex(device_names=["CPU", "GPU"])
        exit(in_t + math_ops.cast(index, dtypes.float32))

    inp = array_ops.placeholder(dtype=dtypes.float32, shape=[1])
    result = computation(inp)
    thread_results = []

    def worker():
        thread_results.extend(sess.run([result], feed_dict={inp: [10.]}))

    worker_thread = threading.Thread(target=worker)
    worker_thread.start()
    main_results = sess.run([result], feed_dict={inp: [20.]})
    worker_thread.join()
    self.assertEqual(thread_results[0], [10 + test_util.is_gpu_available()])
    self.assertEqual(main_results[0], [20 + test_util.is_gpu_available()])
