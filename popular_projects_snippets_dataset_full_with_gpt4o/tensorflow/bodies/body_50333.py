# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save.py
"""Saves a model as a SavedModel to the filepath.

  Args:
    model: Keras model instance to be saved.
    filepath: String path to save the model.
    overwrite: whether to overwrite the existing filepath.
    include_optimizer: If True, save the model's optimizer state.
    signatures: Signatures to save with the SavedModel. Applicable to the 'tf'
      format only. Please see the `signatures` argument in `tf.saved_model.save`
      for details.
    options: (only applies to SavedModel format) `tf.saved_model.SaveOptions`
      object that specifies options for saving to SavedModel.
    save_traces: (only applies to SavedModel format) When enabled, the
      SavedModel will store the function traces for each layer. This
      can be disabled, so that only the configs of each layer are stored.
      Defaults to `True`. Disabling this will decrease serialization time
      and reduce file size, but it requires that all custom layers/models
      implement a `get_config()` method.

  Raises:
    ValueError: if the model's inputs have not been defined.
  """
# If file exists and should not be overwritten.
if not overwrite and os.path.exists(filepath):
    proceed = ask_to_proceed_with_overwrite(filepath)
    if not proceed:
        exit()

if save_traces:
    if save_impl.should_skip_serialization(model):
        saving_utils.raise_model_input_error(model)

if not include_optimizer:
    orig_optimizer = model.optimizer
    model.optimizer = None
    # TODO(b/180760306) Change to del model.optimizer if Layer's __delattr__
    # calls AutoTrackable's __delattr__.
    model._delete_tracking("optimizer")  # pylint: disable=protected-access

# Trace all functions and signatures with `training=0` instead of using an
# already-set learning phase placeholder.
# This is needed for compatibility reasons until learning phase setting
# is removed from the public apis.
with K.deprecated_internal_learning_phase_scope(0):
    with utils.keras_option_scope(save_traces):
        saved_nodes, node_paths = save_lib.save_and_return_nodes(
            model, filepath, signatures, options)

    # Save all metadata to a separate file in the SavedModel directory.
    metadata = generate_keras_metadata(saved_nodes, node_paths)

with gfile.GFile(
    os.path.join(filepath, constants.SAVED_METADATA_PATH), "wb") as w:
    w.write(metadata.SerializeToString(deterministic=True))

if not include_optimizer:
    model.optimizer = orig_optimizer
