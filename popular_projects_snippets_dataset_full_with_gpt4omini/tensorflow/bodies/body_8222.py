# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Saves a checkpoint if a preemption signal has been made available.

    This method works for both tf.distribute.MultiWorkerMirroredStrategy and
    tf.distribute.TPUStrategy. However, this method will add a synchronization
    point between worker and coordinator in the use case of TPUStrategy. If this
    is a concern, use `watch_error_scope` and `run` instead.

    ```python
    strategy = tf.distribute.TPUStrategy()
    # initialization omitted

    with strategy.scope():
      # Save in the checkpoint.
      trained_step = tf.Variable(initial_value=tf.constant(0, dtype=tf.dtypes.int64), name='trained_step', aggregation=tf.VariableAggregation.ONLY_FIRST_REPLICA)

      checkpoint_manager = tf.train.CheckpointManager(checkpoint, directory, max_to_keep=1)
      preemption_handler = tf.distribute.experimental.PreemptionCheckpointHandler(cluster_resolver, checkpoint_manager)

    while trained_step.numpy() < NUM_STEPS:
      train_multi_step_function()
      preemption_handler.save_checkpoint_if_preempted()
    ```

    Args:
      *args: args for `tf.train.CheckpointManager.save()` to save checkpoint.
      **kwargs: kwargs for `tf.train.CheckpointManager.save()` to save.
    """
# pylint: enable=line-too-long
if (self._platform_device ==
    failure_handling_util.PlatformDevice.INTERNAL_TPU):

    try:
        with context.async_scope():
            gen_check_preemption_op.check_preemption(
                preemption_key=PREEMPTION_KEY)
    except errors.AbortedError as abort_error:
        if abort_error.experimental_payloads.get(
            b'type.googleapis.com/tensorflow.distributed_runtime.WorkerPreemption'
        ):
            logging.info('Clearing preemption error to save checkpoint...')

            context.async_clear_error()
            self._save_checkpoint(*args, **kwargs)

            # For TPU training, the default behavior is that it will block until
            # workers are down and returns with error.
            self._exit_fn()

        else:
            raise

else:
    self._check_preemption_and_maybe_checkpoint(*args, **kwargs)
    self._run_counter += 1
    self._estimated_run_time = 0
