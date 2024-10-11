# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_nd_op_test.py
with self.cached_session():
    v = variables.RefVariable(constant_op.constant([[1, 2], [3, 4], [5, 6]]))
    self.evaluate(variables.global_variables_initializer())
    gather = array_ops.gather_nd(v, [[0, 1], [2, 0]])
    if not context.executing_eagerly():  # .op doesn't make sense in Eager
        self.assertEqual("GatherNd", gather.op.name)
    self.assertAllEqual([2, 5], gather)
