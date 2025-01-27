# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_ls_op_test.py
run_gpu_test = test_lib.is_gpu_available(True)
regularizer = 1.0
for matrix_shape in self.matrix_shapes:
    for num_rhs in 1, 2, matrix_shape[-1]:

        with ops.Graph().as_default(), \
            session.Session(config=benchmark.benchmark_config()) as sess, \
            ops.device("/cpu:0"):
            matrix, rhs = _GenerateTestData(matrix_shape, num_rhs)
            x = linalg_ops.matrix_solve_ls(matrix, rhs, regularizer)
            self.evaluate(variables.global_variables_initializer())
            self.run_op_benchmark(
                sess,
                control_flow_ops.group(x),
                min_iters=25,
                store_memory_usage=False,
                name=("matrix_solve_ls_cpu_shape_{matrix_shape}_num_rhs_{num_rhs}"
                     ).format(matrix_shape=matrix_shape, num_rhs=num_rhs))

        if run_gpu_test and (len(matrix_shape) < 3 or matrix_shape[0] < 513):
            with ops.Graph().as_default(), \
                session.Session(config=benchmark.benchmark_config()) as sess, \
                ops.device("/gpu:0"):
                matrix, rhs = _GenerateTestData(matrix_shape, num_rhs)
                x = linalg_ops.matrix_solve_ls(matrix, rhs, regularizer)
                self.evaluate(variables.global_variables_initializer())
                self.run_op_benchmark(
                    sess,
                    control_flow_ops.group(x),
                    min_iters=25,
                    store_memory_usage=False,
                    name=("matrix_solve_ls_gpu_shape_{matrix_shape}_num_rhs_"
                          "{num_rhs}").format(
                              matrix_shape=matrix_shape, num_rhs=num_rhs))
