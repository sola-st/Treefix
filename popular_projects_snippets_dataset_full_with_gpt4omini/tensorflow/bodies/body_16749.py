# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
if scope_name in self.variable_scopes_count:
    self.variable_scopes_count[scope_name] += 1
else:
    self.variable_scopes_count[scope_name] = 1
