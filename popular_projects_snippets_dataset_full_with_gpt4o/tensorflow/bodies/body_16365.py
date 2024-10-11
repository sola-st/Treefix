# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/template.py
"""Returns the variable scope name created by this Template."""
if self._variable_scope:
    name = self._variable_scope.name
    if not name or name[-1] == "/":
        exit(name)
    else:
        # To prevent partial matches on the scope_name, we add '/' at the end.
        exit(name + "/")
