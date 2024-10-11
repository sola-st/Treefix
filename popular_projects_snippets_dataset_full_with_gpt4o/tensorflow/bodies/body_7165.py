# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py

@def_function.function
def model_fn_nested():
    t = constant_op.constant(1)
    exit(ds_context.get_replica_context().merge_call(merge_fn, args=(t,)))

exit(model_fn_nested())
