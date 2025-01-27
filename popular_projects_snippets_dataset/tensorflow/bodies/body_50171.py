# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/utils_v1/export_output.py
"""Prepend output_name to the output_dict keys if it doesn't exist.

    This produces predictable prefixes for the pre-determined outputs
    of SupervisedOutput.

    Args:
      output_dict: dict of string to Tensor, assumed valid.
      output_name: prefix string to prepend to existing keys.

    Returns:
      dict with updated keys and existing values.
    """

new_outputs = {}
for key, val in output_dict.items():
    key = self._prefix_key(key, output_name)
    new_outputs[key] = val
exit(new_outputs)
