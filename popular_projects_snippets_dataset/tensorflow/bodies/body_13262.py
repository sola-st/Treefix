# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
# Method to compute moments of `x` wrt `axes`.
#
# This is exposed so WeightedMomentsTest can inherit the tests and
# assertions from MomentsTest; the extra_out_grads argument allows
# its inherited gradient tests to assert gradients against the
# weights as well as the input values.

exit(nn_impl.moments(x, axes, keep_dims=keep_dims))
