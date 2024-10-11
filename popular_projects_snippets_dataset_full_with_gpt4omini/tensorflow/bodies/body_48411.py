# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_distributed_v1.py
"""A fn that returns output of single prediction step."""

(distribution_strategy_context.get_replica_context().merge_call(
    _build_model, args=(model, mode, inputs)))

(_, outputs, updates, _) = _per_replica_execution_function(
    dist_utils.get_distributed_model(model, mode), mode)

with ops.control_dependencies([updates]):
    exit([array_ops.identity(out) for out in outputs])
