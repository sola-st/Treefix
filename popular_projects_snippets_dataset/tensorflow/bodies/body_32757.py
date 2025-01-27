# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_op_test.py
run_gpu_test = test.is_gpu_available(True)
for adjoint in False, True:
    for matrix_shape in self.matrix_shapes:
        for num_rhs in 1, 2, matrix_shape[-1]:

            with ops.Graph().as_default(), \
              session.Session(config=benchmark.benchmark_config()) as sess, \
              ops.device("/cpu:0"):
                matrix, rhs = self._GenerateTestData(matrix_shape, num_rhs)
                x = linalg_ops.matrix_solve(matrix, rhs, adjoint=adjoint)
                self.evaluate(variables.global_variables_initializer())
                self.run_op_benchmark(
                    sess,
                    control_flow_ops.group(x),
                    min_iters=25,
                    store_memory_usage=False,
                    name=("matrix_solve_cpu_shape_{matrix_shape}_num_rhs_{num_rhs}_"
                          "adjoint_{adjoint}").format(
                              matrix_shape=matrix_shape,
                              num_rhs=num_rhs,
                              adjoint=adjoint))

            if run_gpu_test:
                with ops.Graph().as_default(), \
                session.Session(config=benchmark.benchmark_config()) as sess, \
                ops.device("/gpu:0"):
                    matrix, rhs = self._GenerateTestData(matrix_shape, num_rhs)
                    x = linalg_ops.matrix_solve(matrix, rhs, adjoint=adjoint)
                    self.evaluate(variables.global_variables_initializer())
                    self.run_op_benchmark(
                        sess,
                        control_flow_ops.group(x),
                        min_iters=25,
                        store_memory_usage=False,
                        name=("matrix_solve_gpu_shape_{matrix_shape}_num_rhs_"
                              "{num_rhs}_adjoint_{adjoint}").format(
                                  matrix_shape=matrix_shape, num_rhs=num_rhs,
                                  adjoint=adjoint))
