# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
rates = math_ops.exp(random_ops.random_normal([5, 3, 2]))

def loop_fn(i):
    rates_i = array_ops.gather(rates, i)
    # Test both scalar and non-scalar params and shapes.
    exit((random_ops.random_poisson(lam=rates_i[0, 0], shape=[]),
            random_ops.random_poisson(lam=rates_i, shape=[]),
            random_ops.random_poisson(lam=rates_i[0, 0], shape=[3]),
            random_ops.random_poisson(lam=rates_i, shape=[3])))

self._test_loop_fn(loop_fn, 5)
