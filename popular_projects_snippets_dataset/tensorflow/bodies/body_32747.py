# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
devices = [('/cpu:0', 'cpu')]
if test.is_gpu_available(cuda_only=True):
    devices += [('/gpu:0', 'gpu')]

for device_option, size_option in itertools.product(devices, self.sizes):
    device_id, device_name = device_option
    m, batch_size, n = size_option

    with ops.Graph().as_default(), \
            session.Session(config=benchmark.benchmark_config()) as sess, \
            ops.device(device_id):
        upper, diag, lower, vec = self._generateData(batch_size, m, n)
        x1 = self.baseline(upper, diag, lower, vec)
        x2 = linalg_impl.tridiagonal_matmul((upper, diag, lower),
                                            vec,
                                            diagonals_format='sequence')

        self.evaluate(variables.global_variables_initializer())
        self.run_op_benchmark(
            sess,
            control_flow_ops.group(x1),
            min_iters=10,
            store_memory_usage=False,
            name=('tridiagonal_matmul_baseline_%s'
                  '_batch_size_%d_m_%d_n_%d' %
                  (device_name, batch_size, m, n)))

        self.run_op_benchmark(
            sess,
            control_flow_ops.group(x2),
            min_iters=10,
            store_memory_usage=False,
            name=('tridiagonal_matmul_%s_batch_size_%d_m_%d_n_%d' %
                  (device_name, batch_size, m, n)))
