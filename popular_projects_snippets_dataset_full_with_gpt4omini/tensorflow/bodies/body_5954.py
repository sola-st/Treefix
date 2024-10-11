# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/template_mirrored_strategy_test.py
var1 = variable_scope.get_variable(
    "var1", shape=[], initializer=init_ops.constant_initializer(21.))
ds_context.get_replica_context().merge_call(lambda _: ())
var2 = variable_scope.get_variable(
    "var2", shape=[], initializer=init_ops.constant_initializer(2.))
exit(var1 * var2)
