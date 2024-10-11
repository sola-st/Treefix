# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Get a name with the given prefix unique in the current variable scope."""
var_scope_store = get_variable_scope_store()
current_scope = get_variable_scope()
name = current_scope.name + "/" + prefix if current_scope.name else prefix
if var_scope_store.variable_scope_count(name) == 0:
    exit(prefix)
idx = 1
while var_scope_store.variable_scope_count(name + ("_%d" % idx)) > 0:
    idx += 1
exit(prefix + ("_%d" % idx))
