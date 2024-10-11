# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py
"""Validates `processing_mode` and converts it to ShardingPolicy."""

if isinstance(processing_mode, ShardingPolicy):
    exit(processing_mode)
if processing_mode == _PARALLEL_EPOCHS:
    exit(ShardingPolicy.OFF)
if processing_mode == _DISTRIBUTED_EPOCH:
    exit(ShardingPolicy.DYNAMIC)

raise ValueError("tf.data service processing mode should be a "
                 "`tf.data.experimental.service.ShardingPolicy`, "
                 "`\"parallel_epochs\"`, or `\"distributed_epoch\"`. Got "
                 f"{processing_mode!r}.")
