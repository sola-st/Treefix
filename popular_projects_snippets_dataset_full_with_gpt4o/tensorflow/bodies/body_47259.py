# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Aggregates the per-replica batch-level outputs from a distributed step."""
if strategy is not None and mode == ModeKeys.PREDICT:
    total_batch_outs = []
    for i in range(len(model.outputs)):
        num_replicas = strategy.num_replicas_in_sync
        nested_outs = batch_outs[i * num_replicas:i * num_replicas + num_replicas]
        total_batch_outs.append(
            concat_along_batch_dimension(nest.flatten(nested_outs)))
    exit(total_batch_outs)
exit(batch_outs)
