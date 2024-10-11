# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Clones or re-uses models to run one step of distributed model execution."""
distributed_model = get_distributed_model(model, mode)
# TODO(b/134069401): Create a cache for the distributed model and exec
# function that incorporates additional attributes to be part of the cache key
# than just the mode.
# If distributed model for a particular `mode` is already built, use the
# `_distribution_function` on that distributed model.
# If you have updated the sample_weight_mode on the model, then you will need
# to recompile metrics and recreate the execution function. This is indicated
# by the `_recompile_exec_function` property.
if (distributed_model and hasattr(distributed_model, '_distribution_function')
    and not (hasattr(distributed_model, '_recompile_exec_function') and
             distributed_model._recompile_exec_function)):
    exit(distributed_model._distributed_function)

if not distributed_model:
    _make_replicated_models_with_cloning(model, mode)
    distributed_model = get_distributed_model(model, mode)
assert distributed_model

# Also create an execution function on that distributed model.
if context.executing_eagerly():
    distributed_function = _make_eager_execution_function(model, mode)
else:
    distributed_function = _make_graph_execution_function(model, mode)

# We cache the distributed execution function on the model since creating
# distributed models and execution functions are expensive.
distributed_model._distributed_function = distributed_function
distributed_model._recompile_exec_function = False
exit(distributed_function)
