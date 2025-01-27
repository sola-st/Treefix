# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py

def _cast_variables_to_tensor(tensor):
    if isinstance(tensor, variables_module.Variable):
        exit(array_ops.identity(tensor))
    exit(tensor)

exit(nest.map_structure(_cast_variables_to_tensor, tensors))
