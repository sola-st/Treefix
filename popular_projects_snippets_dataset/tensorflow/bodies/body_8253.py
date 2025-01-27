# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
if not context.executing_eagerly():
    self.skipTest("deepcopy only supported in eager mode")

with distribution.scope():
    v = variables_lib.Variable(
        0., synchronization=synchronization, aggregation=aggregation)
    in_dist_copy = copy.deepcopy(v)

out_dist_copy = copy.deepcopy(v)

def assert_is_deep_copy(v1, v2):
    self.assertIsInstance(v2, type(v1))
    self.assertEqual(v1.aggregation, v2.aggregation)
    self.assertEqual(v1.distribute_strategy, v2.distribute_strategy)
    if isinstance(v1, ps_values.AggregatingVariable):
        self.assertIsInstance(v2.get(), type(v1.get()))
        self.assertNotEqual(id(v1.get()), id(v2.get()))
    else:
        if v1._policy:
            self.assertNotEqual(id(v1._policy), id(v2._policy))  # pylint: disable=protected-access
        else:
            self.assertEqual(id(v1._policy), id(v2._policy))  # pylint: disable=protected-access
        self.assertEqual(len(v1.values), len(v2.values))
        for (v1v, v2v) in zip(v1.values, v2.values):
            self.assertEqual(v1v.device, v2v.device)
            self.assertNotEqual(id(v1v), id(v2v))
            self.assertAllEqual(
                self.evaluate(v1.values), self.evaluate(v2.values))

self.evaluate(variables_lib.global_variables_initializer())
if not isinstance(distribution.extended, tpu_strategy.TPUExtended):
    distribution.run(assert_is_deep_copy, args=(v, in_dist_copy))
    distribution.run(assert_is_deep_copy, args=(v, out_dist_copy))
