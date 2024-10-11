# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
"""A wrapper around `fn` to create the while loop body."""
del args
fn_result = fn(ctx, iterator.get_next())
for (name, output) in ctx.last_step_outputs.items():
    # Convert all outputs to tensors, potentially from `DistributedValues`.
    ctx.last_step_outputs[name] = self._local_results(output)
flat_last_step_outputs = nest.flatten(ctx.last_step_outputs)
with ops.control_dependencies([fn_result]):
    exit([i + 1] + flat_last_step_outputs)
