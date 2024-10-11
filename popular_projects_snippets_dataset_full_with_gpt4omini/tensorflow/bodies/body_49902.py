# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizers.py
"""Inverse of the `serialize` function.

  Args:
      config: Optimizer configuration dictionary.
      custom_objects: Optional dictionary mapping names (strings) to custom
        objects (classes and functions) to be considered during deserialization.

  Returns:
      A Keras Optimizer instance.
  """
# loss_scale_optimizer has a direct dependency of optimizer, import here
# rather than top to avoid the cyclic dependency.
from tensorflow.python.keras.mixed_precision import loss_scale_optimizer  # pylint: disable=g-import-not-at-top
all_classes = {
    'adadelta': adadelta_v2.Adadelta,
    'adagrad': adagrad_v2.Adagrad,
    'adam': adam_v2.Adam,
    'adamax': adamax_v2.Adamax,
    'nadam': nadam_v2.Nadam,
    'rmsprop': rmsprop_v2.RMSprop,
    'sgd': gradient_descent_v2.SGD,
    'ftrl': ftrl.Ftrl,
    'lossscaleoptimizer': loss_scale_optimizer.LossScaleOptimizer,
    # LossScaleOptimizerV1 deserializes into LossScaleOptimizer, as
    # LossScaleOptimizerV1 will be removed soon but deserializing it will
    # still be supported.
    'lossscaleoptimizerv1': loss_scale_optimizer.LossScaleOptimizer,
}

# Make deserialization case-insensitive for built-in optimizers.
if config['class_name'].lower() in all_classes:
    config['class_name'] = config['class_name'].lower()
exit(deserialize_keras_object(
    config,
    module_objects=all_classes,
    custom_objects=custom_objects,
    printable_module_name='optimizer'))
