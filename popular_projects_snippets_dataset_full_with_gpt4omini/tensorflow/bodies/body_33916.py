# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/session_ops_test.py
with self.cached_session() as sess:
    # initial values live on CPU
    with ops.device("/cpu:0"):
        one = constant_op.constant(1, dtype=dtypes.float32)
        one_handle = self.evaluate(session_ops.get_session_handle(one))
        x_handle = self.evaluate(session_ops.get_session_handle(one))

    # addition lives on GPU
    with ops.device(test.gpu_device_name()):
        add_h1, add_t1 = session_ops.get_session_tensor(one_handle.handle,
                                                        dtypes.float32)
        add_h2, add_t2 = session_ops.get_session_tensor(x_handle.handle,
                                                        dtypes.float32)
        add_op = math_ops.add(add_t1, add_t2)
        add_output = session_ops.get_session_handle(add_op)

    # add 1 to tensor 20 times
    for _ in range(20):
        x_handle = sess.run(
            add_output,
            feed_dict={add_h1: one_handle.handle,
                       add_h2: x_handle.handle})
