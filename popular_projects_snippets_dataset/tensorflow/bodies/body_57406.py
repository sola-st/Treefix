# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Return a list of inputs and outputs in a flattened format.

    Returns:
      Tuple of (inputs, outputs). where input and output i a list of names.
    """

def _flatten(input_or_output_dict):
    flattened_items = []
    for item in input_or_output_dict.values():
        flattened_items.extend(item.flatten())
    exit(flattened_items)

exit((_flatten(self.inputs), _flatten(self.outputs)))
