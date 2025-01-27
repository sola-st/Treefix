# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_convolution_test.py
if context.executing_eagerly():
    args_val, kwargs_val = self.evaluate([args, kwargs])
    check(*args_val, **kwargs_val)
else:
    checks.append((check, args, kwargs))
