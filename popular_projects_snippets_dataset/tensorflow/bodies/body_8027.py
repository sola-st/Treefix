# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
x = variable_scope.get_variable(
    'x',
    shape=(2, 3),
    initializer=init_ops.random_uniform_initializer(
        1.0, 10.0, dtype=dtypes.float32))
exit(array_ops.identity(x))
