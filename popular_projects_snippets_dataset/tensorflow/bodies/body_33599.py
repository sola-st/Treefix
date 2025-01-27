# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/determinant_op_test.py
for shape in self.shapes:
    with ops.Graph().as_default(), session.Session(
        config=benchmark.benchmark_config()) as sess, ops.device("/cpu:0"):
        matrix = self._GenerateMatrix(shape)
        d = linalg_ops.matrix_determinant(matrix)
        self.evaluate(variables.global_variables_initializer())
        self.run_op_benchmark(
            sess,
            control_flow_ops.group(
                d,),
            min_iters=25,
            name="matrix_determinant_cpu_{shape}".format(shape=shape))

    if test.is_gpu_available(True):
        with ops.Graph().as_default(), session.Session(
            config=benchmark.benchmark_config()) as sess, ops.device("/gpu:0"):
            matrix = self._GenerateMatrix(shape)
            d = linalg_ops.matrix_determinant(matrix)
            self.evaluate(variables.global_variables_initializer())
            self.run_op_benchmark(
                sess,
                control_flow_ops.group(
                    d,),
                min_iters=25,
                name="matrix_determinant_gpu_{shape}".format(shape=shape))
