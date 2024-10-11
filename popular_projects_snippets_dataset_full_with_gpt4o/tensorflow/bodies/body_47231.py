# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Calculate the number of batches and steps/steps_per_epoch.

  Args:
    distribution_strategy: The DistributionStrategy used to compile the model.
    num_samples: The number of samples from which we determine the batch size
      and steps.
    steps:  The specified number of steps.
    batch_size: The specified batch_size.
    mode: ModeKey representing whether input will be used for training,
      evaluation, or prediction. This is used to relax the constraints on
      consuming all the training samples to keep compatibility till we support
      partial batches. If none, then partial batches are not allowed.

  Returns:
    steps: The steps or steps_per_epoch argument depending on if a user is
        calling `fit`, `evaluate` or `predict`. If the is_training flag is set
        we don't require the number of samples to be used completely.
    batch_size: The batch size to be used in model iterations.

  Raises:
    ValueError: If the number of batches or steps evaluates to 0.

  """
# TODO(b/118776054): Use global batch size for Keras/DS support.
# Currently this is only supported in TPUStrategy and CoreMirroredStrategy.
use_per_replica_batch = not dist_utils.global_batch_size_supported(
    distribution_strategy)

# TODO(b/128995245): In eager mode, uneven batch sizes are allowed except for
# `fit()` on TPUStrategy.
# In graph mode, the zero batch case in batch norm is not handled due to
# XLA-GPU regression. Uneven batch sizes are not allowed except
# for `test()` and `predict()` on TPUStrategy.
if context.executing_eagerly():
    allow_partial_batch = (
        mode != ModeKeys.TRAIN or
        not backend.is_tpu_strategy(distribution_strategy))
else:
    allow_partial_batch = (
        mode == ModeKeys.TRAIN or
        ((mode == ModeKeys.PREDICT or mode == ModeKeys.TEST) and
         backend.is_tpu_strategy(distribution_strategy)))

if steps is None:
    if batch_size is None:
        # If neither the batch size or number of steps are set. We choose the
        # global batch size as the minimum of number of samples and 32. 32 is
        # chosen to provide backward compatibility.
        global_batch_size = min(num_samples, 32)
    else:
        # If the user provided the batch size we need to handle the case
        # between different strategies that use the global/per-replica batch size
        global_batch_size = batch_size
        if use_per_replica_batch:
            global_batch_size *= distribution_strategy.num_replicas_in_sync
    if allow_partial_batch:
        steps = np.ceil(num_samples / global_batch_size).astype(int)
    else:
        if num_samples % global_batch_size:
            raise ValueError('The number of samples %s is not divisible by '
                             'batch size %s.' % (num_samples, global_batch_size))
        steps = num_samples // global_batch_size
else:
    if batch_size is None:
        # We calculate the batch size based on the number of steps specified
        if num_samples % steps:
            raise ValueError('The number of samples %s is not divisible by '
                             'steps %s. Please change the number of steps to a '
                             'value that can consume all the samples' % (
                                 num_samples, steps))
        global_batch_size = num_samples // steps
    else:
        # If the user provided the batch size we need to handle the case
        # between different strategies that use the global/per-replica batch size
        global_batch_size = batch_size
        if use_per_replica_batch:
            global_batch_size *= distribution_strategy.num_replicas_in_sync

        min_num_samples = global_batch_size * steps
        if allow_partial_batch:
            min_num_samples = global_batch_size * (steps-1) + 1 if steps > 1 else 0

        if num_samples < min_num_samples:
            raise ValueError('Number of samples %s is less than samples required '
                             'for specified batch_size %s and steps %s' % (
                                 num_samples, global_batch_size, steps))

  # We need to return the per replica or global batch size based on the strategy
if use_per_replica_batch:
    if global_batch_size % distribution_strategy.num_replicas_in_sync:
        raise ValueError(
            'The batch size (%s) could not be sharded evenly across the sync '
            'replicas (%s) in the distribution strategy.' % (
                global_batch_size, distribution_strategy.num_replicas_in_sync))
    batch_size = global_batch_size // distribution_strategy.num_replicas_in_sync
else:
    batch_size = global_batch_size

exit((steps, batch_size))
