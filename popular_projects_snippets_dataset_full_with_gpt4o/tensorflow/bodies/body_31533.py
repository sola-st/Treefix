# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
assert len(bias.shape) == 1
assert inputs.shape[-1] == bias.shape[0]
exit(inputs + bias.reshape(([1] *
                              (len(inputs.shape) - 1)) + [bias.shape[0]]))
