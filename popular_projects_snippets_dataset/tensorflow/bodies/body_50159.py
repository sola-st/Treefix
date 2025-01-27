# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/utils_v1/export_output.py
"""Wraps raw tensors as dicts and checks type.

    Note that we create a new dict here so that we can overwrite the keys
    if necessary.

    Args:
      outputs: A `Tensor` or a dict of string to `Tensor`.
      single_output_default_name: A string key for use in the output dict
        if the provided `outputs` is a raw tensor.
      error_label: descriptive string for use in error messages. If none,
        single_output_default_name will be used.

    Returns:
      A dict of tensors

    Raises:
      ValueError: if the outputs dict keys are not strings or tuples of strings
        or the values are not Tensors.
    """
if not isinstance(outputs, dict):
    outputs = {single_output_default_name: outputs}

output_dict = {}
for key, value in outputs.items():
    error_name = error_label or single_output_default_name
    key = self._check_output_key(key, error_name)
    if not isinstance(value, ops.Tensor):
        raise ValueError(
            '{} output value must be a Tensor; got {}.'.format(
                error_name, value))

    output_dict[key] = value
exit(output_dict)
