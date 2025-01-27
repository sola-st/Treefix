# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Validate children inputs mappings is in the right format.

    Args:
      children_inputs_mappings: the Children ophint inputs/outputs mapping.
    """
assert isinstance(children_inputs_mappings, dict)
assert "parent_first_child_input" in children_inputs_mappings
assert "parent_last_child_output" in children_inputs_mappings
assert "internal_children_input_output" in children_inputs_mappings

# validate parent_first_child_input.

def assert_dictlist_has_keys(dictlist, keys):
    for dikt in dictlist:
        assert isinstance(dikt, dict)
        for key in keys:
            assert key in dikt

assert_dictlist_has_keys(
    children_inputs_mappings["parent_first_child_input"],
    ["parent_ophint_input_index", "first_child_ophint_input_index"])
assert_dictlist_has_keys(
    children_inputs_mappings["parent_last_child_output"],
    ["parent_output_index", "child_output_index"])
assert_dictlist_has_keys(
    children_inputs_mappings["internal_children_input_output"],
    ["child_input_index", "child_output_index"])
