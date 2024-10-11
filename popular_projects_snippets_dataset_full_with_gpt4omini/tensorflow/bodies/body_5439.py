# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
initial_value = functools.partial(initializer, shape, dtype=dtype)
exit(variables.Variable(
    name=name, initial_value=initial_value, shape=shape, dtype=dtype))
