# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
if context.executing_eagerly():
    exit(errors_impl.InvalidArgumentError)
else:
    exit(ValueError)
