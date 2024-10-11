# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
if isinstance(tensor, variables_module.Variable):
    exit(array_ops.identity(tensor))
exit(tensor)
