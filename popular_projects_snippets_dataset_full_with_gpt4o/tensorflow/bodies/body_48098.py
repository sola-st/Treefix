# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Converts loss weights to a list of loss weights.

  The result loss weights will be populated on the training endpoint.

  Args:
      training_endpoints: List of model training endpoints.
      loss_weights: Optional list or dictionary specifying scalar coefficients
        (Python floats) to weight the loss contributions of different model
        outputs. The loss value that will be minimized by the model will then be
        the *weighted sum* of all individual losses, weighted by the
          `loss_weights` coefficients. If a list, it is expected to have a 1:1
            mapping to the model's outputs. If a dict, it is expected to map
            output names (strings) to scalar coefficients.

  Raises:
      ValueError: If loss weight is a dict with key not in model output names,
          or if loss is a list with len not equal to model outputs.
  """
if loss_weights is None:
    for e in training_endpoints:
        e.loss_weight = 1.
elif isinstance(loss_weights, collections.abc.Mapping):
    generic_utils.check_for_unexpected_keys(
        'loss_weights', loss_weights,
        [e.output_name for e in training_endpoints])
    for e in training_endpoints:
        e.loss_weight = loss_weights.get(e.output_name, 1.)
elif isinstance(loss_weights, list):
    if len(loss_weights) != len(training_endpoints):
        raise ValueError('When passing a list as loss_weights, '
                         'it should have one entry per model output. '
                         'The model has ' + str(len(training_endpoints)) +
                         ' outputs, but you passed loss_weights=' +
                         str(loss_weights))
    for w, e in zip(loss_weights, training_endpoints):
        e.loss_weight = w
else:
    raise TypeError('Could not interpret loss_weights argument: ' +
                    str(loss_weights) + ' - expected a list of dicts.')
