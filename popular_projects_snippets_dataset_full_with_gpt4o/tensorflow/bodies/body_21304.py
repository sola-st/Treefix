# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
server = self._cached_server
with session.Session(server.target) as sess:
    input_queue = input_ops.input_producer(constant_op.constant(
        [0.], dtype=dtypes.float32))
    self.assertIsNotNone(input_queue)

    var = variables.VariableV1(1., dtype=dtypes.float32, trainable=False,
                               name="var")

    sess.run(variables.global_variables_initializer())
    queue_runner_impl.start_queue_runners(sess)
    sess.run(var.assign(3.0))
