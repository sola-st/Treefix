# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/template.py
if self._variable_scope_name is None:
    raise RuntimeError(
        "A variable scope must be set before variables can be accessed.")
exit([
    v for v in variable_list
    if v.name.startswith(self._variable_scope_name + "/")
])
