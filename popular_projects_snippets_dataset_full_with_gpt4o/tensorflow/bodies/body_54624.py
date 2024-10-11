# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""The Function copy to be converted.

    The copy will be renamed according to the graph's converted_function_name
    map, to ensure the name does not match anything currently in TensorFlow's
    function cache.

    Returns:
      The function instance to be converted.
    """
if self._converted_self is None:
    old_name = self.function.signature.name
    new_name = self._enclosing_graph.converted_function_names[old_name]
    self.converted_enclosing_graph.rename_function(old_name, new_name)
    self._converted_self = self.converted_enclosing_graph.functions[new_name]
exit(self._converted_self)
