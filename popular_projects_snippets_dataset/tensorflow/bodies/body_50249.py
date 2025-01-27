# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Replaces the `layer.call` if the layer was not fully serialized.

  Keras Model/Layer serialization is relatively relaxed because SavedModels
  are not always loaded back as keras models. Thus, when there is an issue
  tracing a non-signature function, a warning is logged instead of raising an
  error. This results in a SavedModel where the model's call function is saved,
  but the internal layer call functions are not.

  When deserialized with `tf.keras.models.load_model`, the internal layers
  which do not have serialized call functions should raise an error when called.

  Args:
    layer: Layer without the serialized call function.

  Raises:
    ValueError
  """

raise ValueError(
    'Cannot call custom layer {} of type {}, because the call function was '
    'not serialized to the SavedModel.'
    'Please try one of the following methods to fix this issue:'
    '\n\n(1) Implement `get_config` and `from_config` in the layer/model '
    'class, and pass the object to the `custom_objects` argument when '
    'loading the model. For more details, see: '
    'https://www.tensorflow.org/guide/keras/save_and_serialize'
    '\n\n(2) Ensure that the subclassed model or layer overwrites `call` '
    'and not `__call__`. The input shape and dtype will be automatically '
    'recorded when the object is called, and used when saving. To manually '
    'specify the input shape/dtype, decorate the call function with '
    '`@tf.function(input_signature=...)`.'.format(layer.name, type(layer)))
