# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
def in_cross_replica(_):
    c = variable_scope.variable(1.0, name="c")
    exit(c)

def model_fn():
    b = variable_scope.variable(1.0, name="b")
    with ops.name_scope("foo"):
        c = ds_context.get_replica_context().merge_call(in_cross_replica)
    exit((b, c))

with context.graph_mode(), distribution.scope():
    with ops.name_scope("main"):
        a = variable_scope.variable(1.0, name="a")
        result = distribution.extended.call_for_each_replica(model_fn)
    result_b = result[0]
    result_c = result[1]
    self.assertIsInstance(result_b, values.DistributedValues)
    self.assertIsInstance(result_c, values.DistributedValues)
    a0, a1 = distribution.experimental_local_results(a)
    b0, b1 = distribution.experimental_local_results(result_b)
    c0, c1 = distribution.experimental_local_results(result_c)
    self.assertEqual("main/a:0", a0.name)
    self.assertEqual("main/a/replica_1:0", a1.name)
    self.assertEqual("main/b:0", b0.name)
    self.assertEqual("main/b/replica_1:0", b1.name)
    self.assertEqual("main/foo/c:0", c0.name)
    self.assertEqual("main/foo/c/replica_1:0", c1.name)
