# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
"""Utitlity for create variables that works like variable in keras layer."""
initializer = functools.partial(
    init_ops_v2.GlorotUniform(), shape, dtype=dtype)
exit(variables.Variable(
    initial_value=initializer, name=name, trainable=True))
