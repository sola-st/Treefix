# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Create a OpHint.

    Args:
      function_name: Name of the function (the custom op name in tflite)
      level: OpHint level.
      children_inputs_mappings: Children OpHint inputs/outputs mapping.
        children_inputs_mappings should like below:
        "parent_first_child_input":
            [{"parent_input_index": num, "child_input_index": num}, ...]
        "parent_last_child_output":
            [{"parent_output_index": num, "child_output_index": num}, ...]
        "internal_children_input_output":
            [{"child_input_index": num, "child_output_index": num}, ...]
      **kwargs: Keyword arguments of any constant attributes for the function.
    """
self._function_name = function_name
self._level = level
if self._level == 1:
    assert children_inputs_mappings is None
else:
    assert isinstance(children_inputs_mappings, dict)
self._children_inputs_mappings = children_inputs_mappings
if self._children_inputs_mappings is not None:
    self._validate_children_inputs_mappings(self._children_inputs_mappings)
self._unique_function_id = _uuid.uuid1().hex
self._attrs_to_store_later = kwargs
self._stored_attrs = False
self._inputs = OpHint.OpHintArgumentTracker(
    self._function_name, self._unique_function_id, "InputHint",
    OpHint.FUNCTION_INPUT_INDEX_ATTR, level, self._children_inputs_mappings)
self._outputs = OpHint.OpHintArgumentTracker(
    self._function_name, self._unique_function_id, "OutputHint",
    OpHint.FUNCTION_OUTPUT_INDEX_ATTR, level,
    self._children_inputs_mappings)
