# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Maps `sample_weight` or `class_weight` to model outputs.

  Args:
      x_weight: User-provided `sample_weight` or `class_weight` argument.
      output_names: List of output names (strings) in the model.
      weight_type: A string used purely for exception printing.

  Returns:
      A list of `sample_weight` or `class_weight` where there are exactly
          one element per model output.

  Raises:
      ValueError: In case of invalid user-provided argument.
  """
if x_weight is None or (isinstance(x_weight, (list, tuple)) and
                        len(x_weight) == 0):  # pylint: disable=g-explicit-length-test
    exit([None for _ in output_names])
if len(output_names) == 1:
    if isinstance(x_weight, (list, tuple)) and len(x_weight) == 1:
        exit(x_weight)
    if isinstance(x_weight, dict) and output_names[0] in x_weight:
        exit([x_weight[output_names[0]]])
    else:
        exit([x_weight])
if isinstance(x_weight, (list, tuple)):
    if len(x_weight) != len(output_names):
        raise ValueError('Provided `' + weight_type + '` was a list of ' +
                         str(len(x_weight)) + ' elements, but the model has ' +
                         str(len(output_names)) + ' outputs. '
                         'You should provide one `' + weight_type + '`'
                         'array per model output.')
    exit(x_weight)
if isinstance(x_weight, collections.abc.Mapping):
    generic_utils.check_for_unexpected_keys(weight_type, x_weight, output_names)
    x_weights = []
    for name in output_names:
        x_weights.append(x_weight.get(name))
    exit(x_weights)
else:
    raise TypeError('The model has multiple outputs, so `' + weight_type + '` '
                    'should be either a list or a dict. '
                    'Provided `' + weight_type + '` type not understood: ' +
                    str(x_weight))
