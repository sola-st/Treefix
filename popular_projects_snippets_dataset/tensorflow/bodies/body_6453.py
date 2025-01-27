# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
with distribution.scope():
    v1 = variables_lib.Variable(
        [1, 1, 1], aggregation=variables_lib.VariableAggregation.SUM)
    v2 = variables_lib.Variable([1, 1, 1])
self.evaluate(variables_lib.global_variables_initializer())

value = indexed_slices.IndexedSlices(
    values=array_ops.identity([2]),
    indices=array_ops.identity([0]),
    dense_shape=(3,))
with distribution.scope():
    self.evaluate(v1.scatter_add(value))
    self.assertAllEqual([3, 1, 1], self.evaluate(v1.read_value()))

    self.evaluate(v2.scatter_min(value))
    self.assertAllEqual([1, 1, 1], self.evaluate(v2.read_value()))
