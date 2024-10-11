# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_distributed_v1.py
"""A step fn that returns update ops."""
if isinstance(inputs, (tuple, list)) and len(inputs) == 2:
    inputs, targets = inputs
else:
    targets = None

# When input feature is a dictionary of tensors, dictionary is flattended
# to an array and passed as a model input. This results in input mismatch
# when model input layer names are not sorted in alphabetical order as
# `nest.flatten()`sorts dictionary elements by keys. As so, transform input
# tensors into an array and order it along `model._feed_input_names`.
if isinstance(inputs, dict):
    inputs = [inputs[input_name] for input_name in model._feed_input_names]

_build_model(strategy, model, mode, inputs, targets)

(grouped_inputs, grouped_outputs, grouped_updates,
 grouped_session_args) = strategy.extended.call_for_each_replica(
     _per_replica_execution_function,
     args=(dist_utils.get_distributed_model(model, mode), mode))
(all_inputs, all_outputs, all_updates,
 all_session_args) = dist_utils.unwrap_values(strategy, grouped_inputs,
                                              grouped_outputs,
                                              grouped_updates,
                                              grouped_session_args)
combined_fn = backend.function(
    all_inputs,
    all_outputs,
    updates=all_updates,
    name='distributed_' + str(mode) + '_function',
    **all_session_args)

for label, output in zip(output_labels, combined_fn.outputs):
    if label == 'loss':
        reduce_op = ds_reduce_util.ReduceOp.SUM
    else:
        # We reduce all other metrics using mean for now. This is temporary
        # workaround until new metrics are in place.
        reduce_op = ds_reduce_util.ReduceOp.MEAN
    ctx.set_last_step_output(label, output, reduce_op)

# TODO(priyag, sourabhbajaj): Ignoring these things from the combined_fn:
# feed_dict, session kwargs, run options, run_metadata for now. These should
# be handled appropriately
exit(combined_fn.updates_op)
