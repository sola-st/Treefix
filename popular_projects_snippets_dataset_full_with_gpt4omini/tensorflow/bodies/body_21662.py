# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation_test.py
exit(variable_scope.get_variable(
    name,
    dtype=dtypes.float32,
    initializer=init_value,
    trainable=False,
    collections=[ops.GraphKeys.LOCAL_VARIABLES]))
