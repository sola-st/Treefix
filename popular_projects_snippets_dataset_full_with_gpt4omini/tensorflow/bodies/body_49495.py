# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/losses_utils.py
exit(control_flow_ops.cond(
    math_ops.equal(rank_diff, 1), maybe_squeeze_weights,
    _maybe_expand_weights))
