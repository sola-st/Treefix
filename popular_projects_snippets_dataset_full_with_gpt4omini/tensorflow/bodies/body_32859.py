# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
for shape_ in self.shapes:
    with ops.Graph().as_default(), \
          session.Session(config=benchmark.benchmark_config()) as sess, \
          ops.device("/cpu:0"):
        matrix_value = np.random.uniform(
            low=-1.0, high=1.0, size=shape_).astype(np.float32)
        matrix = variables.Variable(matrix_value)
        u, s, v = linalg_ops.svd(matrix)
        self.evaluate(variables.global_variables_initializer())
        self.run_op_benchmark(
            sess,
            control_flow_ops.group(u, s, v),
            min_iters=25,
            name="SVD_cpu_{shape}".format(shape=shape_))

    if test.is_gpu_available(True):
        with ops.Graph().as_default(), \
            session.Session(config=benchmark.benchmark_config()) as sess, \
            ops.device("/device:GPU:0"):
            matrix_value = np.random.uniform(
                low=-1.0, high=1.0, size=shape_).astype(np.float32)
            matrix = variables.Variable(matrix_value)
            u, s, v = linalg_ops.svd(matrix)
            self.evaluate(variables.global_variables_initializer())
            self.run_op_benchmark(
                sess,
                control_flow_ops.group(u, s, v),
                min_iters=25,
                name="SVD_gpu_{shape}".format(shape=shape_))
