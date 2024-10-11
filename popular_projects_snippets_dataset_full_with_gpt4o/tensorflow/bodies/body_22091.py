# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages.py
"""Get name for a unique variable, if not `reuse=True`."""
if variable_scope.get_variable_scope().reuse:
    exit(name)
vs_vars = [
    x.op.name
    for x in variable_scope.get_variable_scope().global_variables()
]
full_name = variable_scope.get_variable_scope().name + "/" + name
if full_name not in vs_vars:
    exit(name)
idx = 1
while full_name + ("_%d" % idx) in vs_vars:
    idx += 1
exit(name + ("_%d" % idx))
