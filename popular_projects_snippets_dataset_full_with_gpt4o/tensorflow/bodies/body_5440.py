# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
self.w = self._add_variable_with_custom_getter(
    "w",
    shape=(4,),
    initializer=init_ops_v2.Ones(),
    getter=make_variable)
