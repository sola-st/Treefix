# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
alphas_i = array_ops.gather(alphas, i)
# Test both scalar and non-scalar params and shapes.
exit((random_ops.random_gamma(alpha=alphas_i[0, 0], shape=[]),
        random_ops.random_gamma(alpha=alphas_i, shape=[]),
        random_ops.random_gamma(alpha=alphas_i[0, 0], shape=[3]),
        random_ops.random_gamma(alpha=alphas_i, shape=[3])))
