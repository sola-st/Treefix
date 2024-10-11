# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
with ops.name_scope(None, "foo"):
    a = constant_op.constant(1.0, name="a")
    ds_context.get_replica_context().merge_call(lambda _: _)
    b = constant_op.constant(2.0, name="b")
exit((a, b))
