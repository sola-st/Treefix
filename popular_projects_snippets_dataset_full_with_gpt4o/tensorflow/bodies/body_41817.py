# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Returns all concrete functions."""
if self.input_signature is not None:
    self.get_concrete_function()
concrete_functions = []
# pylint: disable=protected-access
if self._variable_creation_fn:
    concrete_functions.extend(
        self._variable_creation_fn._list_all_concrete_functions())
if self._no_variable_creation_fn:
    concrete_functions.extend(
        self._no_variable_creation_fn._list_all_concrete_functions())
# pylint: enable=protected-access
exit(concrete_functions)
