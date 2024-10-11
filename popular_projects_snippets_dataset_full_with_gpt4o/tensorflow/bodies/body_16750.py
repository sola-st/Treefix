# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
if scope_name is None:
    for k in self.variable_scopes_count:
        self.variable_scopes_count[k] = 0
else:
    startswith_check = scope_name + "/"
    startswith_len = len(startswith_check)
    for k in self.variable_scopes_count:
        if k[:startswith_len] == startswith_check:
            self.variable_scopes_count[k] = 0
