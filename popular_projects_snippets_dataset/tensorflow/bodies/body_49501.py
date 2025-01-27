# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/losses_utils.py
"""Scales and returns the given loss value by the number of replicas."""
num_replicas = (
    distribution_strategy_context.get_strategy().num_replicas_in_sync)
if num_replicas > 1:
    loss_value *= (1. / num_replicas)
exit(loss_value)
