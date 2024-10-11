# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py

def model_fn():
    vs = []
    vs.append(variable_scope.variable(1.0, name="foo/bar"))
    vs.append(variable_scope.variable(1.0, name="foo_1/bar"))
    vs.append(variable_scope.variable(1.0, name="foo_1/bar_1"))
    vs.append(variable_scope.variable(1.0, name="foo/bar_1"))
    ds_context.get_replica_context().merge_call(lambda _: _)
    exit(vs)

with distribution.scope():
    result = distribution.extended.call_for_each_replica(model_fn)
    for v in result:
        self.assertTrue(distribute_utils.is_mirrored(v))
    self.assertEqual(4, len(result))
    self.assertEqual("foo/bar:0", result[0].name)
    self.assertEqual("foo_1/bar:0", result[1].name)
    self.assertEqual("foo_1/bar_1:0", result[2].name)
    self.assertEqual("foo/bar_1:0", result[3].name)
