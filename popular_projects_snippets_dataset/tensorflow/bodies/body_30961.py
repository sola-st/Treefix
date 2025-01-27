# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/cudnn_deterministic_base.py
# np.random.random_sample can properly interpret either tf.TensorShape or
# namedtuple as a list.
exit(constant_op.constant(
    2 * np.random.random_sample(shape) - 1, dtype=dtypes.float32))
