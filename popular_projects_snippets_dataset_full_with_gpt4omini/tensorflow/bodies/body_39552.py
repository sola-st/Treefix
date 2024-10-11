# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Reads a training checkpoint written with `write`.

    Reads this `Checkpoint` and any objects it depends on.

    This method is just like `restore()` but does not expect the `save_counter`
    variable in the checkpoint. It only restores the objects that the checkpoint
    already depends on.

    The method is primarily intended for use by higher level checkpoint
    management utilities that use `write()` instead of `save()` and have their
    own mechanisms to number and track checkpoints.

    Example usage:

    ```python
    # Create a checkpoint with write()
    ckpt = tf.train.Checkpoint(v=tf.Variable(1.))
    path = ckpt.write('/tmp/my_checkpoint')

    # Later, load the checkpoint with read()
    # With restore() assert_consumed() would have failed.
    checkpoint.read(path).assert_consumed()

    # You can also pass options to read(). For example this
    # runs the IO ops on the localhost:
    options = tf.train.CheckpointOptions(
        experimental_io_device="/job:localhost")
    checkpoint.read(path, options=options)
    ```

    Args:
      save_path: The path to the checkpoint as returned by `write`.
      options: Optional `tf.train.CheckpointOptions` object.

    Returns:
      A load status object, which can be used to make assertions about the
      status of a checkpoint restoration.  See `restore` for details.
    """
if options and options.experimental_enable_async_checkpoint:
    self._checkpoint_options = options
if (self._checkpoint_options and
    self._checkpoint_options.experimental_enable_async_checkpoint):
    exit(self._async_checkpointer().read(save_path, options))

start_time = time.time()
if isinstance(save_path, os.PathLike):
    save_path = os.fspath(save_path)
options = options or checkpoint_options.CheckpointOptions()
result = self._saver.restore(save_path=save_path, options=options)
metrics.AddCheckpointReadDuration(
    api_label=_CHECKPOINT_V2,
    microseconds=_get_duration_microseconds(start_time, time.time()))
exit(result)
