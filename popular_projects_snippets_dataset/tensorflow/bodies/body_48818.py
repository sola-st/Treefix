# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Saves all layer weights.

    Either saves in HDF5 or in TensorFlow format based on the `save_format`
    argument.

    When saving in HDF5 format, the weight file has:
      - `layer_names` (attribute), a list of strings
          (ordered names of model layers).
      - For every layer, a `group` named `layer.name`
          - For every such layer group, a group attribute `weight_names`,
              a list of strings
              (ordered names of weights tensor of the layer).
          - For every weight in the layer, a dataset
              storing the weight value, named after the weight tensor.

    When saving in TensorFlow format, all objects referenced by the network are
    saved in the same format as `tf.train.Checkpoint`, including any `Layer`
    instances or `Optimizer` instances assigned to object attributes. For
    networks constructed from inputs and outputs using `tf.keras.Model(inputs,
    outputs)`, `Layer` instances used by the network are tracked/saved
    automatically. For user-defined classes which inherit from `tf.keras.Model`,
    `Layer` instances must be assigned to object attributes, typically in the
    constructor. See the documentation of `tf.train.Checkpoint` and
    `tf.keras.Model` for details.

    While the formats are the same, do not mix `save_weights` and
    `tf.train.Checkpoint`. Checkpoints saved by `Model.save_weights` should be
    loaded using `Model.load_weights`. Checkpoints saved using
    `tf.train.Checkpoint.save` should be restored using the corresponding
    `tf.train.Checkpoint.restore`. Prefer `tf.train.Checkpoint` over
    `save_weights` for training checkpoints.

    The TensorFlow format matches objects and variables by starting at a root
    object, `self` for `save_weights`, and greedily matching attribute
    names. For `Model.save` this is the `Model`, and for `Checkpoint.save` this
    is the `Checkpoint` even if the `Checkpoint` has a model attached. This
    means saving a `tf.keras.Model` using `save_weights` and loading into a
    `tf.train.Checkpoint` with a `Model` attached (or vice versa) will not match
    the `Model`'s variables. See the [guide to training
    checkpoints](https://www.tensorflow.org/guide/checkpoint) for details
    on the TensorFlow format.

    Args:
        filepath: String or PathLike, path to the file to save the weights to.
            When saving in TensorFlow format, this is the prefix used for
            checkpoint files (multiple files are generated). Note that the '.h5'
            suffix causes weights to be saved in HDF5 format.
        overwrite: Whether to silently overwrite any existing file at the
            target location, or provide the user with a manual prompt.
        save_format: Either 'tf' or 'h5'. A `filepath` ending in '.h5' or
            '.keras' will default to HDF5 if `save_format` is `None`. Otherwise
            `None` defaults to 'tf'.
        options: Optional `tf.train.CheckpointOptions` object that specifies
            options for saving weights.

    Raises:
        ImportError: If h5py is not available when attempting to save in HDF5
            format.
        ValueError: For invalid/unknown format arguments.
    """
self._assert_weights_created()
filepath = path_to_string(filepath)
filepath_is_h5 = saving_utils.is_hdf5_filepath(filepath)
if save_format is None:
    if filepath_is_h5:
        save_format = 'h5'
    else:
        save_format = 'tf'
else:
    user_format = save_format.lower().strip()
    if user_format in ('tensorflow', 'tf'):
        save_format = 'tf'
    elif user_format in ('hdf5', 'h5', 'keras'):
        save_format = 'h5'
    else:
        raise ValueError(
            'Unknown format "%s". Was expecting one of {"tf", "h5"}.' % (
                save_format,))
if save_format == 'tf' and filepath_is_h5:
    raise ValueError(
        ('save_weights got save_format="tf"/"tensorflow", but the '
         'filepath ("%s") looks like an HDF5 file. Omit the ".h5"/".keras" '
         'when saving in TensorFlow format.')
        % filepath)

if save_format == 'h5' and h5py is None:
    raise ImportError(
        '`save_weights` requires h5py when saving in hdf5.')
if save_format == 'tf':
    check_filepath = filepath + '.index'
else:
    check_filepath = filepath
# If file exists and should not be overwritten:
if not overwrite and os.path.isfile(check_filepath):
    proceed = ask_to_proceed_with_overwrite(check_filepath)
    if not proceed:
        exit()
if save_format == 'h5':
    with h5py.File(filepath, 'w') as f:
        hdf5_format.save_weights_to_hdf5_group(f, self.layers)
else:
    if not context.executing_eagerly():
        # Call `get_session` to initialize any uninitialized variables.
        backend.get_session()
    self._checkpoint.write(filepath, options=options)
    # Record this checkpoint so it's visible from tf.train.latest_checkpoint.
    checkpoint_management.update_checkpoint_state_internal(
        save_dir=os.path.dirname(filepath),
        model_checkpoint_path=filepath,
        save_relative_paths=True,
        all_model_checkpoint_paths=[filepath])
