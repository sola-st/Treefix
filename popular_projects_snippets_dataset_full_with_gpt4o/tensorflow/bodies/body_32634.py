# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_inverse_op_test.py
for adjoint in False, True:
    for shape in self.shapes:
        with ops.Graph().as_default(), \
            session.Session(config=benchmark.benchmark_config()) as sess, \
            ops.device("/cpu:0"):
            matrix = self._GenerateMatrix(shape)
            inv = linalg_ops.matrix_inverse(matrix, adjoint=adjoint)
            self.evaluate(variables.global_variables_initializer())
            self.run_op_benchmark(
                sess,
                control_flow_ops.group(inv),
                min_iters=25,
                name="matrix_inverse_cpu_{shape}_adjoint_{adjoint}".format(
                    shape=shape, adjoint=adjoint))

        if test.is_gpu_available(True):
            with ops.Graph().as_default(), \
              session.Session(config=benchmark.benchmark_config()) as sess, \
              ops.device("/gpu:0"):
                matrix = self._GenerateMatrix(shape)
                inv = linalg_ops.matrix_inverse(matrix, adjoint=adjoint)
                self.evaluate(variables.global_variables_initializer())
                self.run_op_benchmark(
                    sess,
                    control_flow_ops.group(inv),
                    min_iters=25,
                    name="matrix_inverse_gpu_{shape}_adjoint_{adjoint}".format(
                        shape=shape, adjoint=adjoint))
