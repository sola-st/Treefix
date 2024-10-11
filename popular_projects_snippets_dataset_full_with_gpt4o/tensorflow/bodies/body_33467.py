# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/lu_op_test.py
for shape in self.shapes:
    with ops.Graph().as_default(), \
          session.Session(config=benchmark.benchmark_config()) as sess, \
          ops.device("/cpu:0"):
        matrix = variables.Variable(self._GenerateMatrix(shape))
        lu, p = linalg_ops.lu(matrix)
        self.evaluate(variables.global_variables_initializer())
        self.run_op_benchmark(
            sess,
            control_flow_ops.group(lu, p),
            min_iters=25,
            name="lu_cpu_{shape}".format(shape=shape))

    if test.is_gpu_available(True):
        with ops.Graph().as_default(), \
            session.Session(config=benchmark.benchmark_config()) as sess, \
            ops.device("/device:GPU:0"):
            matrix = variables.Variable(self._GenerateMatrix(shape))
            lu, p = linalg_ops.lu(matrix)
            self.evaluate(variables.global_variables_initializer())
            self.run_op_benchmark(
                sess,
                control_flow_ops.group(lu, p),
                min_iters=25,
                name="lu_gpu_{shape}".format(shape=shape))
