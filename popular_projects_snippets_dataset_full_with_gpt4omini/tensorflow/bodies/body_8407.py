# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Single step on the TPU device."""
fn_result = fn(ctx, inputs)
flat_last_step_outputs = nest.flatten(ctx.last_step_outputs)
if flat_last_step_outputs:
    with ops.control_dependencies([fn_result]):
        exit([array_ops.identity(f) for f in flat_last_step_outputs])
else:
    exit(fn_result)
