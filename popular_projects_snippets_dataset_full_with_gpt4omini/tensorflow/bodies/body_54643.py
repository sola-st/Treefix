# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Initializes a _FunctionCaller.

    Args:
      node: As in _Node.
      function: As in _Node.
      enclosing_graph: As in _Node.
      first_function_input: The index of the first NodeDef input that is tied to
        the function inputs. It is assumed that the rest of the NodeDef inputs
        map one to one to function inputs.
      type_attribute: The name of the NodeDef attribute that defines the input
        types. It is assumed that the types listed here map one-to-one with the
        function inputs (that is, they do _not_ specify types for inputs that
        are not passed to functions).
      function_attributes: The names of the NodeDef attributes containing
        references to functions.
    """
super(_FunctionCaller, self).__init__(node, function, enclosing_graph)
self._first_function_input = first_function_input
self._type_attribute = type_attribute
self._function_attributes = function_attributes
