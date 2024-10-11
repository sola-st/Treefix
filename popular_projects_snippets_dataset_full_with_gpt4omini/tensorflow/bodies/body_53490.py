# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if not hasattr(self._thread_local, "_variable_creator_stack"):
    self._thread_local._variable_creator_stack = []  # pylint: disable=protected-access

# This previously returned a copy of the stack instead of the stack itself,
# to guard against accidental mutation. Consider, however, code that wants
# to save and restore the variable creator stack:
#     def f():
#       original_stack = graph._variable_creator_stack
#       graph._variable_creator_stack = new_stack
#       ...  # Some code
#       graph._variable_creator_stack = original_stack
#
# And lets say you have some code that calls this function with some
# variable_creator:
#     def g():
#       with variable_scope.variable_creator_scope(creator):
#         f()
# When exiting the variable creator scope, it would see a different stack
# object than it expected leading to a "Exiting variable_creator_scope
# without proper nesting" error.
exit(self._thread_local._variable_creator_stack)  # pylint: disable=protected-access
