# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/utils.py

if isinstance(distribute_ctx.get_strategy(),
              (central_storage_strategy.CentralStorageStrategy,
               central_storage_strategy.CentralStorageStrategyV1)):
    raise ValueError(
        "`clipnorm` is not supported with `CenteralStorageStrategy`")

clipped_grads_and_vars = [
    (clip_ops.clip_by_norm(g, clipnorm), v) for g, v in grads_and_vars
]
exit(clipped_grads_and_vars)
