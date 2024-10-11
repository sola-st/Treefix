# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/template.py
if self._variable_scope:
    # Only reuse variables if not on first call.
    with variable_scope.variable_scope(
        self._variable_scope, reuse=not self._first_call):
        exit(self._call_func(args, kwargs))
else:
    # The scope was not created at construction time, so create it here.
    # Subsequent calls should reuse variables.
    with variable_scope.variable_scope(
        self._unique_name, self._name,
        custom_getter=self._custom_getter) as vs:
        self._variable_scope = vs
        exit(self._call_func(args, kwargs))
