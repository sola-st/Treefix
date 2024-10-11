# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model_experimental.py
"""Loads a keras Model from a SavedModel created by `export_saved_model()`.

  This function reinstantiates model state by:
  1) loading model topology from json (this will eventually come
     from metagraph).
  2) loading model weights from checkpoint.

  Example:

  ```python
  import tensorflow as tf

  # Create a tf.keras model.
  model = tf.keras.Sequential()
  model.add(tf.keras.layers.Dense(1, input_shape=[10]))
  model.summary()

  # Save the tf.keras model in the SavedModel format.
  path = '/tmp/simple_keras_model'
  tf.keras.experimental.export_saved_model(model, path)

  # Load the saved keras model back.
  new_model = tf.keras.experimental.load_from_saved_model(path)
  new_model.summary()
  ```

  Args:
    saved_model_path: a string specifying the path to an existing SavedModel.
    custom_objects: Optional dictionary mapping names
        (strings) to custom classes or functions to be
        considered during deserialization.

  Returns:
    a keras.Model instance.
  """
warnings.warn('`tf.keras.experimental.load_from_saved_model` is deprecated'
              'and will be removed in a future version. '
              'Please switch to `tf.keras.models.load_model`.')
# restore model topology from json string
model_json_filepath = os.path.join(
    compat.as_bytes(saved_model_path),
    compat.as_bytes(constants.ASSETS_DIRECTORY),
    compat.as_bytes(SAVED_MODEL_FILENAME_JSON))
with gfile.Open(model_json_filepath, 'r') as f:
    model_json = f.read()
model = model_config.model_from_json(
    model_json, custom_objects=custom_objects)

# restore model weights
checkpoint_prefix = os.path.join(
    compat.as_text(saved_model_path),
    compat.as_text(constants.VARIABLES_DIRECTORY),
    compat.as_text(constants.VARIABLES_FILENAME))
model.load_weights(checkpoint_prefix)
exit(model)
