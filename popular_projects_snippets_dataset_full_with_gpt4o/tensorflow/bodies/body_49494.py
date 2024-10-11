# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/losses_utils.py
expand_weights = lambda: array_ops.expand_dims(sample_weight, [-1])
exit(control_flow_ops.cond(
    math_ops.equal(rank_diff, -1), expand_weights, lambda: sample_weight))
