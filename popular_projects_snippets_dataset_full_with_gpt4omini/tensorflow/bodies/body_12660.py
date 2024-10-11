# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
"""Tests that the unbatch timeout works."""
if context.executing_eagerly():
    exit()
with self.cached_session() as sess:
    inp = array_ops.placeholder(dtype=dtypes.int32, shape=[1])
    batched, index, id_t = batch_ops.batch(
        [inp], num_batch_threads=1, max_batch_size=2,
        batch_timeout_micros=36000000, grad_timeout_micros=0,
        batching_queue="")
    computation = batched[0] + 1
    timeout_micros = 10
    result = batch_ops.unbatch(computation, index, id_t, timeout_micros,
                               shared_name="shared_unbatch")
    # Set up a parallel pipeline that delays the computation, but uses the
    # same unbatch resource object as the non-delayed pipeline.
    computation_delayed = script_ops.py_func(delayed_plus1,
                                             [batched[0]],
                                             dtypes.int32)
    result_delayed = batch_ops.unbatch(computation_delayed,
                                       index,
                                       id_t,
                                       timeout_micros,
                                       shared_name="shared_unbatch")

    thread_results = []
    def worker():
        # A first call using the non-delayed pipeline. The batcher will send an
        # empty tensor along the non-delayed pipeline.
        thread_results.extend(sess.run([result], feed_dict={inp: [1]}))
    worker_thread = threading.Thread(target=worker)
    worker_thread.start()
    time.sleep(0.1)  # Ensure the thread's call starts first.
    # A second call using the delayed pipeline.  The batcher will send the
    # batched tensor along the delayed pipeline, thus delaying the arrival of
    # the batched tensor at the unbatch op, relative to the empty tensor.
    #
    # TODO(olston, apassos): Avoid relying on the order in which the batch op
    # emits the empty tensor versus the batched one.
    _ = sess.run([result_delayed], feed_dict={inp: [2]})
    worker_thread.join()
    # The thread's call should hit the timeout, and thus get 0 results.
    self.assertEqual(len(thread_results), 0)
