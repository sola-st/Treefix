# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduce_benchmark_test.py
with context.eager_mode():
    tensor = array_ops.zeros([100, 1000])

    def fn():
        backprop.gradients_function(math_ops.reduce_sum, [0])(tensor)

    self._run(fn, 10000)
