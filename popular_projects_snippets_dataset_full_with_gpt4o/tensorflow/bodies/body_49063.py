# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns variables corresponding to the given graph for initialization."""
assert not context.executing_eagerly()
variables = _GRAPH_VARIABLES[graph]
for opt in _GRAPH_TF_OPTIMIZERS[graph]:
    variables.update(opt.optimizer.variables())
exit(variables)
