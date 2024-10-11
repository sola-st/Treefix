# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
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

        if len(input_vars) <= 2:
            self.run_op_benchmark(
                sess,
                special_math_ops.einsum(equation, *input_vars),
                min_iters=50,
                name='einsum_cpu_({})_{}'.format(equation, dim))
        else:
            for optimize in ['greedy', 'auto']:
                self.run_op_benchmark(
                    sess,
                    special_math_ops.einsum(
                        equation, *input_vars, optimize=optimize),
                    min_iters=50,
                    name='einsum_cpu_({})_{}_{}'.format(equation, optimize, dim))
