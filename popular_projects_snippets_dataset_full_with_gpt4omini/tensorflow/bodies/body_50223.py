# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Loads Keras objects from a SavedModel.

  Any Keras layer or model saved to the SavedModel will be loaded back
  as Keras objects. Other objects are loaded as regular trackable objects (same
  as `tf.saved_model.load`).

  Currently, Keras saving/loading only retains the Keras object's weights,
  losses, and call function.

  The loaded model can be re-compiled, but the original optimizer, compiled loss
  functions, and metrics are not retained. This is temporary, and `model.save`
  will soon be able to serialize compiled models.

  Args:
    path: Path to SavedModel.
    compile: If true, compile the model after loading it.
    options: Optional `tf.saved_model.LoadOptions` object that specifies
      options for loading from SavedModel.


  Returns:
    Object loaded from SavedModel.
  """
# TODO(kathywu): Add saving/loading of optimizer, compiled losses and metrics.
# TODO(kathywu): Add code to load from objects that contain all endpoints

# Look for metadata file or parse the SavedModel
metadata = saved_metadata_pb2.SavedMetadata()
meta_graph_def = loader_impl.parse_saved_model(path).meta_graphs[0]
object_graph_def = meta_graph_def.object_graph_def
path_to_metadata_pb = os.path.join(path, constants.SAVED_METADATA_PATH)
if gfile.Exists(path_to_metadata_pb):
    try:
        with gfile.GFile(path_to_metadata_pb, 'rb') as f:
            file_content = f.read()
        metadata.ParseFromString(file_content)
    except message.DecodeError as e:
        raise IOError('Cannot parse keras metadata {}: {}.'
                      .format(path_to_metadata_pb, str(e)))
else:
    logging.warning('SavedModel saved prior to TF 2.5 detected when loading '
                    'Keras model. Please ensure that you are saving the model '
                    'with model.save() or tf.keras.models.save_model(), *NOT* '
                    'tf.saved_model.save(). To confirm, there should be a file '
                    'named "keras_metadata.pb" in the SavedModel directory.')
    _read_legacy_metadata(object_graph_def, metadata)

if not metadata.nodes:
    # When there are no Keras objects, return the results from the core loader
    exit(tf_load.load(path, options=options))

# Recreate layers and metrics using the info stored in the metadata.
keras_loader = KerasObjectLoader(metadata, object_graph_def)
keras_loader.load_layers(compile=compile)

# Generate a dictionary of all loaded nodes.
nodes_to_load = {'root': None}
for node_id, loaded_node in keras_loader.loaded_nodes.items():
    nodes_to_load[keras_loader.get_path(node_id)] = loaded_node
loaded = tf_load.load_partial(path, nodes_to_load, options=options)

# Finalize the loaded layers and remove the extra tracked dependencies.
keras_loader.finalize_objects()
keras_loader.del_tracking()

model = loaded['root']

# pylint: disable=protected-access
if isinstance(model, training_lib.Model) and compile:
    # TODO(kathywu): Use compiled objects from SavedModel, instead of
    # creating new objects from the training config.
    training_config = model._serialized_attributes['metadata'].get(
        'training_config', None)
    if training_config is not None:
        model.compile(**saving_utils.compile_args_from_training_config(
            training_config), from_serialized=True)
        saving_utils.try_build_compiled_arguments(model)
        if isinstance(model.optimizer, optimizer_v2.OptimizerV2):
            if (model.optimizer.get_slot_names()):
                logging.warning('Your optimizer uses slots. '
                                'Slots cannot be restored from saved_model, '
                                'as a result, your model is starting with  '
                                'a new initialized optimizer.')
    else:
        logging.warning('No training configuration found in save file, so the '
                        'model was *not* compiled. Compile it manually.')
  # pylint: enable=protected-access

  # Force variables and resources to initialize.
if not context.executing_eagerly():
    sess = backend.get_session()  # Variables are initialized by this call.
    sess.run(ops.get_collection(ops.GraphKeys.TABLE_INITIALIZERS))

exit(model)
