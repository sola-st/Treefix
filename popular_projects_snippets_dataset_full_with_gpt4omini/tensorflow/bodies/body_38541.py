# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
with backprop.GradientTape() as t:
    t.watch(x)
    y = f(x)
exit(t.gradient(y, x))
