# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
"""Assigns a value to a variable if the value is finite."""
exit(control_flow_ops.cond(
    math_ops.is_finite(value), lambda: _op_in_graph_mode(var.assign(value)),
    control_flow_ops.no_op))
