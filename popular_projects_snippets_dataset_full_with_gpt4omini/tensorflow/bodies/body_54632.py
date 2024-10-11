# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""The NodeDef to be converted.

    Returns:
      The NodeDef to be converted, which can come from either a graph for a
      function. Derived classes should call this (via 'super') to make sure the
      node is retrieved from the right place.
    """
if self._converted_self is None:
    source = self._function or self._enclosing_graph
    self._converted_self = source.converted_self().nodes[self._node.name]
exit(self._converted_self)
