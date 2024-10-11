# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_serialization.py
"""Raises error if input type is tf.Variable."""
if any(isinstance(inp, resource_variable_ops.VariableSpec)
       for inp in nest.flatten(
           concrete_function.structured_input_signature)):
    raise ValueError(
        f"Unable to serialize concrete_function '{concrete_function.name}'"
        f"with tf.Variable input. Functions that expect tf.Variable "
        "inputs cannot be exported as signatures.")
