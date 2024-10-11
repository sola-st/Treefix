# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Restores a training checkpoint.

    Restores this `Checkpoint` and any objects it depends on.

    This method is intended to be used to load checkpoints created by `save()`.
    For checkpoints created by `write()` use the `read()` method which does not
    expect the `save_counter` variable added by `save()`.

    `restore()` either assigns values immediately if variables to restore have
    been created already, or defers restoration until the variables are
    created. Dependencies added after this call will be matched if they have a
    corresponding object in the checkpoint (the restore request will queue in
    any trackable object waiting for the expected dependency to be added).

    ```python
    checkpoint = tf.train.Checkpoint( ... )
    checkpoint.restore(path)

    # You can additionally pass options to restore():
    options = tf.CheckpointOptions(experimental_io_device="/job:localhost")
    checkpoint.restore(path, options=options)
    ```

    To ensure that loading is complete and no more deferred restorations will
    take place, use the `assert_consumed()` method of the status object returned
    by `restore()`:

    ```python
    checkpoint.restore(path, options=options).assert_consumed()
    ```

    The assert will raise an error if any Python objects in the dependency graph
    were not found in the checkpoint, or if any checkpointed values do not have
    a matching Python object.

    Name-based `tf.compat.v1.train.Saver` checkpoints from TensorFlow 1.x can be
    loaded using this method. Names are used to match variables. Re-encode
    name-based checkpoints using `tf.train.Checkpoint.save` as soon as possible.

    **Loading from SavedModel checkpoints**

    To load values from a SavedModel, just pass the SavedModel directory
    to checkpoint.restore:

    ```python
    model = tf.keras.Model(...)
    tf.saved_model.save(model, path)  # or model.save(path, save_format='tf')

    checkpoint = tf.train.Checkpoint(model)
    checkpoint.restore(path).expect_partial()
    ```

    This example calls `expect_partial()` on the loaded status, since
    SavedModels saved from Keras often generates extra keys in the checkpoint.
    Otherwise, the program prints a lot of warnings about unused keys at exit
    time.

    Args:
      save_path: The path to the checkpoint, as returned by `save` or
        `tf.train.latest_checkpoint`. If the checkpoint was written by the
        name-based `tf.compat.v1.train.Saver`, names are used to match
        variables. This path may also be a SavedModel directory.
      options: Optional `tf.train.CheckpointOptions` object.

    Returns:
      A load status object, which can be used to make assertions about the
      status of a checkpoint restoration.

      The returned status object has the following methods:

      * `assert_consumed()`:
          Raises an exception if any variables are unmatched: either
          checkpointed values which don't have a matching Python object or
          Python objects in the dependency graph with no values in the
          checkpoint. This method returns the status object, and so may be
          chained with other assertions.

      * `assert_existing_objects_matched()`:
          Raises an exception if any existing Python objects in the dependency
          graph are unmatched. Unlike `assert_consumed`, this assertion will
          pass if values in the checkpoint have no corresponding Python
          objects. For example a `tf.keras.Layer` object which has not yet been
          built, and so has not created any variables, will pass this assertion
          but fail `assert_consumed`. Useful when loading part of a larger
          checkpoint into a new Python program, e.g. a training checkpoint with
          a `tf.compat.v1.train.Optimizer` was saved but only the state required
          for
          inference is being loaded. This method returns the status object, and
          so may be chained with other assertions.

      * `assert_nontrivial_match()`: Asserts that something aside from the root
          object was matched. This is a very weak assertion, but is useful for
          sanity checking in library code where objects may exist in the
          checkpoint which haven't been created in Python and some Python
          objects may not have a checkpointed value.

      * `expect_partial()`: Silence warnings about incomplete checkpoint
          restores. Warnings are otherwise printed for unused parts of the
          checkpoint file or object when the `Checkpoint` object is deleted
          (often at program shutdown).

    Raises:
      NotFoundError: if the a checkpoint or SavedModel cannot be found at
        `save_path`.
    """
if options and options.experimental_enable_async_checkpoint:
    self._checkpoint_options = options
if (self._checkpoint_options and
    self._checkpoint_options.experimental_enable_async_checkpoint):
    exit(self._async_checkpointer().restore(save_path, options))

orig_save_path = save_path
if isinstance(save_path, os.PathLike):
    save_path = os.fspath(save_path)

if save_path is not None and gfile.IsDirectory(save_path) and (
    (gfile.Exists(path_helpers.get_saved_model_pb_path(save_path)) or
     gfile.Exists(path_helpers.get_saved_model_pbtxt_path(save_path)))):
    save_path = path_helpers.get_variables_path(save_path)

try:
    status = self.read(save_path, options=options)
    if context.executing_eagerly():
        context.async_wait()  # Ensure restore operations have completed.
except errors_impl.NotFoundError as e:
    raise errors_impl.NotFoundError(
        None, None,
        f"Error when restoring from checkpoint or SavedModel at "
        f"{orig_save_path}: {e.message}"
        f"\nPlease double-check that the path is correct. You may be missing "
        "the checkpoint suffix (e.g. the '-1' in 'path/to/ckpt-1').")
# Create the save counter now so it gets initialized with other variables
# when graph building. Creating it earlier would lead to errors when using,
# say, train.Saver() to save the model before initializing it.
self._maybe_create_save_counter()
if isinstance(status, NameBasedSaverStatus):
    status.add_to_optionally_restored(self.save_counter)
exit(status)
