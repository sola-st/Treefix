# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/iterator_ops.py
"""Initializes a `CheckpointInputPipelineHook`.

    If the input pipeline depends on external state (e.g. seeds for
    RandomUniform) beyond the input pipeline, this hook would be unable to
    serialize and deserialize that state. If its acceptable to ignore that state
    change the external_state_policy argument to 'warn' or 'ignore'. For e.g.

    ```python
    est = tf.estimator.Estimator(model_fn)
    while True:
      est.train(
          train_input_fn,
          hooks=[tf.data.experimental.CheckpointInputPipelineHook(
              est, external_state_policy='warn')],
          steps=train_steps_per_eval)
      # Note: We do not pass the hook here.
      metrics = est.evaluate(eval_input_fn)
      if should_stop_the_training(metrics):
        break
    ```

    Args:
      estimator: Estimator.
      external_state_policy: A string that identifies how to handle input
        pipelines that depend on external state. Possible values are
        'ignore': The external state is silently ignored.
        'warn': The external state is ignored, logging a warning.
        'fail': The operation fails upon encountering external state.
        By default we set it to 'fail'.

    Raises:
      ValueError: One of `save_steps` or `save_secs` should be set.
      ValueError: At most one of saver or scaffold should be set.
      ValueError: If `external_state_policy` is not one of 'warn', 'ignore' or
        'fail'.
    """
if external_state_policy is None:
    external_state_policy = "fail"
self._external_state_policy = _convert_external_state_policy_to_enum(
    external_state_policy)
# `checkpoint_basename` is "input.ckpt" for non-distributed pipelines or
# of the form "input_<task_type>_<task_id>.ckpt" for distributed pipelines.
# Note: The default `checkpoint_basename` used by `CheckpointSaverHook` is
# "model.ckpt". We intentionally choose the input pipeline checkpoint prefix
# to be different to avoid conflicts with the model checkpoint.

# pylint: disable=protected-access
checkpoint_prefix = "input"
if estimator._config.num_worker_replicas > 1:
    # Distributed setting.
    suffix = "_{}_{}".format(estimator._config.task_type,
                             estimator._config.task_id)
    checkpoint_prefix += suffix
# pylint: enable=protected-access

# We use a composition paradigm instead of inheriting from
# `CheckpointSaverHook` because `Estimator` does an `isinstance` check
# to check whether a `CheckpointSaverHook` is already present in the list
# of hooks and if not, adds one. Inheriting from `CheckpointSaverHook`
# would thwart this behavior. This hook checkpoints *only the iterators*
# and not the graph variables.
self._checkpoint_saver_hook = basic_session_run_hooks.CheckpointSaverHook(
    estimator.model_dir,
    save_secs=estimator._config.save_checkpoints_secs,  # pylint: disable=protected-access
    save_steps=estimator._config.save_checkpoints_steps,  # pylint: disable=protected-access
    checkpoint_basename=checkpoint_prefix + ".ckpt")

# Name for the protocol buffer file that will contain the list of most
# recent checkpoints stored as a `CheckpointState` protocol buffer.
# This file, kept in the same directory as the checkpoint files, is
# automatically managed by the `Saver` to keep track of recent checkpoints.
# The default name used by the `Saver` for this file is "checkpoint". Here
# we use the name "checkpoint_<checkpoint_prefix>" so that in case the
# `checkpoint_dir` is the same as the model checkpoint directory, there are
# no conflicts during restore.
self._latest_filename = "checkpoint_" + checkpoint_prefix
