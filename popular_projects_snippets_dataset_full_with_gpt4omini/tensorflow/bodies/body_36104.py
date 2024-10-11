# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
var = resource_variable_ops.ResourceVariable(1.)
self.evaluate(variables.global_variables_initializer())
assigned = var.assign(2.)
self.assertIsInstance(assigned, resource_variable_ops.BaseResourceVariable)
assigned = assigned.assign(3.)
self.assertEqual(self.evaluate(assigned), 3.)
self.assertEqual(self.evaluate(var), 3.)

self.assertEqual(self.evaluate(var.assign_add(1.).assign_add(1.)), 5)
self.assertEqual(self.evaluate(var.assign_sub(1.).assign_sub(1.)), 3)

var = resource_variable_ops.ResourceVariable([1., 2.])
self.evaluate(variables.global_variables_initializer())
slices = indexed_slices.IndexedSlices(indices=[1], values=[2])
def assert_eq(tensor, vals):
    self.assertAllEqual(self.evaluate(tensor), vals)
assert_eq(var.scatter_add(slices).scatter_add(slices), [1., 6.])
assert_eq(var.scatter_sub(slices).scatter_sub(slices), [1., 2.])
slices2 = indexed_slices.IndexedSlices(indices=[0], values=[3])
assert_eq(var.scatter_max(slices2).scatter_add(slices), [3., 4.])
assert_eq(var.scatter_add(slices).scatter_min(slices), [3., 2.])
assert_eq(var.scatter_mul(slices).scatter_mul(slices), [3., 8.])
assert_eq(var.scatter_div(slices).scatter_div(slices), [3., 2.])
assert_eq(
    var.scatter_nd_update([[1]], [4.]).scatter_nd_add([[0]], [2.])
    .scatter_nd_sub([[1]], [3]),
    [5., 1.])
assert_eq(var, [5., 1.])

batch_var = resource_variable_ops.ResourceVariable(array_ops.ones((2, 2)))
self.evaluate(variables.global_variables_initializer())
batch_slices1 = indexed_slices.IndexedSlices(
    indices=[[1], [0]], values=[[2], [2]])
batch_slices2 = indexed_slices.IndexedSlices(
    indices=[[1], [1]], values=[[3], [3]])
assert_eq(
    batch_var.batch_scatter_update(batch_slices1)
    .batch_scatter_update(batch_slices2),
    [[1, 3], [2, 3]])
