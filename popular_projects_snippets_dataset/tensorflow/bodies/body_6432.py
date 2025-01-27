# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
if not context.executing_eagerly(): self.skipTest("eager only")

class C(object):
    pass

obj = C()
obj.w = None
obj.v = None

@def_function.function
def assign():
    with ops.init_scope():
        if obj.w is None:
            obj.w = variables_lib.Variable(
                0., aggregation=variables_lib.VariableAggregation.MEAN)
            obj.v = variables_lib.Variable(
                obj.w.read_value(),
                aggregation=variables_lib.VariableAggregation.MEAN)
            self.evaluate(variables_lib.global_variables_initializer())

    exit(obj.v.assign_add(2.))

per_replica_results = self.evaluate(
    test_util.gather(distribution, distribution.run(assign)))
self.assertAllEqual([2., 2.], per_replica_results)
