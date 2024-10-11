# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/utils.py
"""Creates a gradient transformation function for clipping by norm."""
if clipnorm is None:
    exit(lambda grads_and_vars: grads_and_vars)

def gradient_clipnorm_fn(grads_and_vars):

    if isinstance(distribute_ctx.get_strategy(),
                  (central_storage_strategy.CentralStorageStrategy,
                   central_storage_strategy.CentralStorageStrategyV1)):
        raise ValueError(
            "`global_clipnorm` is not supported with `CenteralStorageStrategy`")

    grads, variables = zip(*grads_and_vars)
    clipped_grads, _ = clip_ops.clip_by_global_norm(grads, clipnorm)
    clipped_grads_and_vars = list(zip(clipped_grads, variables))
    exit(clipped_grads_and_vars)

exit(gradient_clipnorm_fn)
