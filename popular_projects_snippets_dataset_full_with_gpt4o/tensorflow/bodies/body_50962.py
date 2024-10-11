# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
"""Evaluate a tensor.

    Takes care of the variations between graphs produced with and without
    resource variables when determining the name of the operation to run.

    Args:
      tensor: The tensor to evaluate, or a string with the tensor name.

    Returns:
      The evaluated tensor as a numpy array.
    """
name = tensor if isinstance(tensor, str) else tensor.name
index = "0"
if ":" in name:
    name, index = name.split(":")
if variable_scope.resource_variables_enabled():
    name = name + "/Read/ReadVariableOp"
exit(self.evaluate(name + ":" + index))
