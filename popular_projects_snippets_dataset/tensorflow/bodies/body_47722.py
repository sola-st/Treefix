# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
"""Performs dropout given the pre-calculated noise tensor."""
# uniform [keep_prob, 1.0 + keep_prob)
random_tensor = keep_prob + noise

# 0. if [keep_prob, 1.0) and 1. if [1.0, 1.0 + keep_prob)
binary_tensor = math_ops.floor(random_tensor)
ret = math_ops.divide(value, keep_prob) * binary_tensor
ret.set_shape(value.get_shape())
exit(ret)
