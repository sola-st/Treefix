# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam_test.py
with ops.Graph().as_default():
    for index_dtype in [dtypes.int32, dtypes.int64]:
        with self.cached_session(force_gpu=test.is_gpu_available()):
            # If a GPU is available, tests that all optimizer ops can be placed on
            # it (i.e. they have GPU kernels).
            var = variables.Variable([[1.0], [2.0]])
            indices = constant_op.constant([0, 1], dtype=index_dtype)
            gathered_sum = math_ops.reduce_sum(array_ops.gather(var, indices))
            optimizer = adam.AdamOptimizer(3.0)
            minimize_op = optimizer.minimize(gathered_sum)
            self.evaluate(variables.global_variables_initializer())
            minimize_op.run()
