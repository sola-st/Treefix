# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Converts loss to a list of loss functions.

  Args:
      loss: String (name of objective function), objective function or
        `tf.losses.Loss` instance. See `tf.losses`. If the model has multiple
        outputs, you can use a different loss on each output by passing a
        dictionary or a list of losses. The loss value that will be minimized by
        the model will then be the sum of all individual losses.
      output_names: List of model output names.

  Returns:
      A list of loss objective functions.

  Raises:
      ValueError: If loss is a dict with keys not in model output names,
          or if loss is a list with len not equal to model outputs.
  """
if isinstance(loss, collections.abc.Mapping):
    generic_utils.check_for_unexpected_keys('loss', loss, output_names)
    loss_functions = []
    for name in output_names:
        if name not in loss:
            logging.warning(
                'Output {0} missing from loss dictionary. We assume '
                'this was done on purpose. The fit and evaluate APIs will not be '
                'expecting any data to be passed to {0}.'.format(name))
        loss_functions.append(get_loss_function(loss.get(name, None)))
elif isinstance(loss, str):
    loss_functions = [get_loss_function(loss) for _ in output_names]
elif isinstance(loss, collections.abc.Sequence):
    if len(loss) != len(output_names):
        raise ValueError('When passing a list as loss, it should have one entry '
                         'per model outputs. The model has {} outputs, but you '
                         'passed loss={}'.format(len(output_names), loss))
    loss_functions = nest.map_structure(get_loss_function, loss)
else:
    loss_functions = [get_loss_function(loss) for _ in range(len(output_names))]

exit(loss_functions)
