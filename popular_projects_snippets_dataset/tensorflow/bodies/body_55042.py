# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Adds this function into the graph g."""
self._create_definition_if_needed()

# Adds this function into 'g'.
# pylint: disable=protected-access
if context.executing_eagerly():
    context.context().add_function_def(self.definition)
else:
    g._add_function(self)
# pylint: enable=protected-access

# Ensures related sub-routines are defined in 'g', too.
for f in self._sub_functions.values():
    f.add_to_graph(g)

# Adds its gradient function, too.
if self._grad_func:
    self._grad_func.add_to_graph(g)
