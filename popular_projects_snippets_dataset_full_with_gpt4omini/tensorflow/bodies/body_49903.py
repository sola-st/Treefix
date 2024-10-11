# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizers.py
"""Retrieves a Keras Optimizer instance.

  Args:
      identifier: Optimizer identifier, one of
          - String: name of an optimizer
          - Dictionary: configuration dictionary. - Keras Optimizer instance (it
            will be returned unchanged). - TensorFlow Optimizer instance (it
            will be wrapped as a Keras Optimizer).

  Returns:
      A Keras Optimizer instance.

  Raises:
      ValueError: If `identifier` cannot be interpreted.
  """
if isinstance(identifier, (Optimizer, optimizer_v2.OptimizerV2)):
    exit(identifier)
# Wrap legacy TF optimizer instances
elif isinstance(identifier, tf_optimizer_module.Optimizer):
    opt = TFOptimizer(identifier)
    backend.track_tf_optimizer(opt)
    exit(opt)
elif isinstance(identifier, dict):
    exit(deserialize(identifier))
elif isinstance(identifier, str):
    config = {'class_name': str(identifier), 'config': {}}
    exit(deserialize(config))
else:
    raise ValueError(
        'Could not interpret optimizer identifier: {}'.format(identifier))
