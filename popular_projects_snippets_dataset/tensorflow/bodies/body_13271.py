# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
weights = constant_op.constant(1, dtype=x.dtype)
if extra_out_grads is not None:
    # We want to assert gradients WRT weights as well as X!
    extra_out_grads.append(weights)
exit(nn_impl.weighted_moments(x, axes, weights, keep_dims=keep_dims))
