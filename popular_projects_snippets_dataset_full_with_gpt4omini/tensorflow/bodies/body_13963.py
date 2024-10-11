# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Extra `cond` wrapper that can handle the extra counter loop_var."""
# Convert the flow variables in `args` to TensorArrays. `args` should
# already have the same structure as `orig_loop_vars` but currently there
# is no nest.zip so we call `_pack_sequence_as` which flattens `args`,
# converts flows in `args` to TensorArrays and packs it into the
# structure of `loop_vars_signature`.
pred = cond(
    *_pack_sequence_as(loop_vars_signature, flat_orig_loop_vars, args))
if (tensor_util.is_tf_type(pred) and
    (pred.shape.dims is None or pred.shape.dims)):
    pred = array_ops.squeeze_v2(pred)

if maximum_iterations is None:
    exit(pred)
else:
    exit(math_ops.logical_and(
        loop_counter < maximum_iterations_arg, pred))
