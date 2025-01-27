# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/qr_op_test.py
for shape_ in self.shapes:
    with ops.Graph().as_default(), \
          session.Session(config=benchmark.benchmark_config()) as sess, \
          ops.device("/cpu:0"):
        matrix_value = np.random.uniform(
            low=-1.0, high=1.0, size=shape_).astype(np.float32)
        matrix = variables.Variable(matrix_value)
        q, r = linalg_ops.qr(matrix)
        self.evaluate(variables.global_variables_initializer())
        self.run_op_benchmark(
            sess,
            control_flow_ops.group(q, r),
            min_iters=25,
            name="QR_cpu_{shape}".format(shape=shape_))

    if test.is_gpu_available(True):
        with ops.Graph().as_default(), \
            session.Session(config=benchmark.benchmark_config()) as sess, \
            ops.device("/device:GPU:0"):
            matrix_value = np.random.uniform(
                low=-1.0, high=1.0, size=shape_).astype(np.float32)
            matrix = variables.Variable(matrix_value)
            q, r = linalg_ops.qr(matrix)
            self.evaluate(variables.global_variables_initializer())
            self.run_op_benchmark(
                sess,
                control_flow_ops.group(q, r),
                min_iters=25,
                name="QR_gpu_{shape}".format(shape=shape_))
