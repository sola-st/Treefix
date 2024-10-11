# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/hdf5_format.py
"""Saves a model to a HDF5 file.

  The saved model contains:
      - the model's configuration (topology)
      - the model's weights
      - the model's optimizer's state (if any)

  Thus the saved model can be reinstantiated in
  the exact same state, without any of the code
  used for model definition or training.

  Args:
      model: Keras model instance to be saved.
      filepath: One of the following:
          - String, path where to save the model
          - `h5py.File` object where to save the model
      overwrite: Whether we should overwrite any existing
          model at the target location, or instead
          ask the user with a manual prompt.
      include_optimizer: If True, save optimizer's state together.

  Raises:
      ImportError: if h5py is not available.
  """

if h5py is None:
    raise ImportError('`save_model` requires h5py.')

# TODO(psv) Add warning when we save models that contain non-serializable
# entities like metrics added using `add_metric` and losses added using
# `add_loss.`
if len(model.weights) != len(model._undeduplicated_weights):
    logging.warning('Found duplicated `Variable`s in Model\'s `weights`. '
                    'This is usually caused by `Variable`s being shared by '
                    'Layers in the Model. These `Variable`s will be treated '
                    'as separate `Variable`s when the Model is restored. To '
                    'avoid this, please save with `save_format="tf"`.')

if not isinstance(filepath, h5py.File):
    # If file exists and should not be overwritten.
    if not overwrite and os.path.isfile(filepath):
        proceed = ask_to_proceed_with_overwrite(filepath)
        if not proceed:
            exit()

    # Try creating dir if not exist
    dirpath = os.path.dirname(filepath)
    if not os.path.exists(dirpath):
        gfile.MakeDirs(dirpath)

    f = h5py.File(filepath, mode='w')
    opened_new_file = True
else:
    f = filepath
    opened_new_file = False

try:
    model_metadata = saving_utils.model_metadata(model, include_optimizer)
    for k, v in model_metadata.items():
        if isinstance(v, (dict, list, tuple)):
            f.attrs[k] = json.dumps(
                v, default=json_utils.get_json_type).encode('utf8')
        else:
            f.attrs[k] = v

    model_weights_group = f.create_group('model_weights')
    model_layers = model.layers
    save_weights_to_hdf5_group(model_weights_group, model_layers)

    # TODO(b/128683857): Add integration tests between tf.keras and external
    # Keras, to avoid breaking TF.js users.
    if (include_optimizer and model.optimizer and
        not isinstance(model.optimizer, optimizer_v1.TFOptimizer)):
        save_optimizer_weights_to_hdf5_group(f, model.optimizer)

    f.flush()
finally:
    if opened_new_file:
        f.close()
