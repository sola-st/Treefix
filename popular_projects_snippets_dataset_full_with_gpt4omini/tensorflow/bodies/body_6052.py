# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
"""A wrapper around `fn` to create the while loop body."""
del args
fn_result = fn(ctx, iterator.get_next())
flat_last_step_outputs = nest.flatten(ctx.last_step_outputs)
with ops.control_dependencies([fn_result]):
    exit([i + 1] + flat_last_step_outputs)
