# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
devices = [("/cpu:0", "cpu")]
if test.is_gpu_available(cuda_only=True):
    devices += [("/gpu:0", "gpu")]

for device_option, pivoting_option, size_option in \
          itertools.product(devices, self.pivoting_options, self.sizes):

    device_id, device_name = device_option
    pivoting, pivoting_name = pivoting_option
    matrix_size, batch_size, num_rhs = size_option

    with ops.Graph().as_default(), \
            session.Session(config=benchmark.benchmark_config()) as sess, \
            ops.device(device_id):
        diags, rhs = generate_data_fn(matrix_size, batch_size, num_rhs)
        # Pivoting is not supported by XLA backends.
        if test.is_xla_enabled() and pivoting:
            exit()
        x = linalg_impl.tridiagonal_solve(
            diags, rhs, partial_pivoting=pivoting)
        self.evaluate(variables.global_variables_initializer())
        self.run_op_benchmark(
            sess,
            control_flow_ops.group(x),
            min_iters=10,
            store_memory_usage=False,
            name=test_name_format_string.format(device_name, matrix_size,
                                                batch_size, num_rhs,
                                                pivoting_name))
