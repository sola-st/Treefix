# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

def model_fn(name):
    v = variable_scope.variable(1.0, name=name)
    ds_context.get_replica_context().merge_call(lambda _: _)
    exit(v)

with distribution.scope():
    names = values.PerReplica(("foo", "bar"))
    with self.assertRaises(RuntimeError):
        _ = distribution.extended.call_for_each_replica(model_fn, args=(names,))
