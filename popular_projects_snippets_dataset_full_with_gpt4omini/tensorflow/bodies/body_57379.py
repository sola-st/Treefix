# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Initialize ophint argument.

      Args:
        function_name: Name of the function that this tracks arguments for.
        unique_function_id: UUID of function that this tracks arguments for.
        node_name_prefix: How identities that are created are named.
        attr_name: Name of attribute to use to store the index for this hint.
          i.e. FUNCTION_INPUT_INDEX or FUNCTION_OUTPUT_INDEX
        level: Hierarchical level of the Ophint node, a number.
        children_inputs_mappings: Inputs/Outputs mapping for children hints.
      """

# The global index is the argument index of the op. This is in contrast
# to the sort index which is the sequence number of a particular instance
# of a given global index. For example, you may have called add hint
# twice with the tag "foo". Then the global index will be 0 for both
# and the sort index will be 0 for the first added and 1 for the second.
self._function_name = function_name
self._unique_function_id = unique_function_id
self._next_global_index = 0  # The absolute global index
self._used_global_indices = set()
self._tag_to_global_index = {}  # The argument index a given tag maps to
self._tag_to_next_sort_index = {}  # The current index for each tag
self._node_name_prefix = node_name_prefix
self._attr_name = attr_name
self._level = level
self._children_inputs_mappings = children_inputs_mappings
