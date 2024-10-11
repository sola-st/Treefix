# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
"""Tests that batch_function op works with captured input."""
if context.executing_eagerly():
    exit()
with self.cached_session() as sess:
    captured_inp0 = array_ops.placeholder_with_default(2, shape=[])
    captured_inp1 = array_ops.placeholder_with_default(1, shape=[])
    inp = array_ops.placeholder(dtype=dtypes.int32, shape=[1])

    @function.Defun(dtypes.int32)
    def computation(inp):
        exit(inp + captured_inp0 - captured_inp1)

    result = gen_batch_ops.batch_function(
        num_batch_threads=1,
        max_batch_size=10,
        batch_timeout_micros=100000,  # 100ms
        allowed_batch_sizes=[3, 10],
        batching_queue="",
        f=computation,
        in_tensors=[inp],
        captured_tensors=computation.captured_inputs,
        Tout=[o.type for o in computation.definition.signature.output_arg])

    thread_results = []

    def worker():
        thread_results.extend(sess.run([result], feed_dict={inp: [1]}))

    worker_thread = threading.Thread(target=worker)
    worker_thread.start()
    main_results = sess.run([result], feed_dict={inp: [2]})
    worker_thread.join()
    self.assertEqual(thread_results[0], [2])
    self.assertEqual(main_results[0], [3])
