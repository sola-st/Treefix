# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
log_prob = math_ops.xlogy(a - 1., x) - math_ops.lgamma(a) - x
prob = math_ops.exp(log_prob)
exit(-gen_math_ops.igamma_grad_a(a, x) / prob)
