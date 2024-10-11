# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
super(_VariableScopeStore, self).__init__()
self.current_scope = VariableScope(False)
self.variable_scopes_count = {}
