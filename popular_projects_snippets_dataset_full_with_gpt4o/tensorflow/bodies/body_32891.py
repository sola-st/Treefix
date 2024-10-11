# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
for equation, dim in self.cases:
    with ops.Graph().as_default(), \
          session.Session(config=benchmark.benchmark_config()) as sess, \
          ops.device('/cpu:0'):
        r = np.random.RandomState(0)
        input_subscripts = equation.split('->')[0].split(',')
        input_vars = []
        for subscript in input_subscripts:
            input_shape = (dim,) * len(subscript)
            input_vars.append(
                variables.Variable(np.array(r.randn(*input_shape), np.float32)))
        self.evaluate(variables.global_variables_initializer())

        # Call einsum_v1.
        self.run_op_benchmark(
            sess,
            special_math_ops.einsum(equation, *input_vars),
            min_iters=50,
            name='einsum_v1_cpu_({})_{}'.format(equation, dim))

        # Call gen_linalg_ops.einsum.
        self.run_op_benchmark(
            sess,
            gen_linalg_ops.einsum(input_vars, equation),
            min_iters=50,
            name='einsum_v2_cpu_({})_{}'.format(equation, dim))
