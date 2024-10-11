# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/batch_matmul_op_test.py
for (a_shape, b_shape) in self.shape_pairs:
    with ops.Graph().as_default(), \
          session.Session(config=benchmark.benchmark_config()) as sess, \
          ops.device("/cpu:0"):
        matrix_a = variables.Variable(
            GetRandomNormalInput(a_shape, np.float32))
        matrix_b = variables.Variable(
            GetRandomNormalInput(b_shape, np.float32))
        self.evaluate(variables.global_variables_initializer())

        # Use batch matmul op's internal broadcasting.
        self.run_op_benchmark(
            sess,
            math_ops.matmul(matrix_a, matrix_b),
            min_iters=50,
            name="batch_matmul_cpu_{}_{}".format(a_shape, b_shape))

        # Manually broadcast the input matrices using the broadcast_to op.
        broadcasted_batch_shape = array_ops.broadcast_static_shape(
            matrix_a.shape[:-2], matrix_b.shape[:-2])
        broadcasted_a_shape = broadcasted_batch_shape.concatenate(
            matrix_a.shape[-2:])
        broadcasted_b_shape = broadcasted_batch_shape.concatenate(
            matrix_b.shape[-2:])
        self.run_op_benchmark(
            sess,
            math_ops.matmul(
                array_ops.broadcast_to(matrix_a, broadcasted_a_shape),
                array_ops.broadcast_to(matrix_b, broadcasted_b_shape)),
            min_iters=50,
            name="batch_matmul_manual_broadcast_cpu_{}_{}".format(
                a_shape, b_shape))
