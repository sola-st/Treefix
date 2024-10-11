# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils.py
exit((isinstance(x, variables.Variable) or
        resource_variable_ops.is_resource_variable(x)))
