# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batch_scatter_ops_test.py
var = variables.Variable([True, False])
update0 = state_ops.batch_scatter_update(var, [1], [True])
update1 = state_ops.batch_scatter_update(
    var, constant_op.constant(
        [0], dtype=dtypes.int64), [False])
self.evaluate(variables.variables_initializer([var]))

self.evaluate([update0, update1])

self.assertAllEqual([False, True], self.evaluate(var))
