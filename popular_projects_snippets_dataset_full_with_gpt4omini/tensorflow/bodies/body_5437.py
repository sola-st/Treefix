# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
if not collection:
    identity = init_ops_v2.Identity()
    v1 = variables.Variable([[1., 0.], [0., 1.]], dtype=dtypes.float32)
    v2 = variables.Variable(lambda: identity((2, 2), dtypes.float32))
    v3 = variables.Variable(
        lambda: identity((2, 2), dtypes.float32),
        dtype=dtypes.float32,
        shape=(2, 2))
    collection.extend([v1, v2, v3])
