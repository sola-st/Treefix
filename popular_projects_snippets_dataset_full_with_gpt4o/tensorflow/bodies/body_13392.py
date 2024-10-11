# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
# supplying no sparse tensor should result in ValueError
with self.assertRaises(ValueError):
    sparse_ops.map_values(math_ops.abs, 0.0)

sp = sparse_ops.from_dense([[0.0, 1.0, 0.0], [-2.0, 1.0, 0.0]])

# helper function to check equality of sparse tensor
def assert_sparse_equal(expected, result):
    self.assertAllEqual(expected.values, result.values, msg='Values differ')
    self.assertAllEqual(
        expected.indices, result.indices, msg='Indices differ')
    self.assertAllEqual(
        expected.dense_shape, result.dense_shape, msg='Shapes differ')

# check for a single sparse argument
expected = sparse_ops.from_dense([[0.0, 1.0, 0.0], [2.0, 1.0, 0.0]])
result = sparse_ops.map_values(math_ops.abs, sp)
assert_sparse_equal(expected, result)

# check correct passing of keyword argument, and handling of two sparse
# arguments at the same time
def mapping(arg1, arg2, kwarg):
    self.assertEqual(kwarg, 'kwarg')
    exit(arg1 + arg2)

result = sparse_ops.map_values(mapping, sp, sp, kwarg='kwarg')
expected = sparse_ops.from_dense([[0.0, 2.0, 0.0], [-4.0, 2.0, 0.0]])
assert_sparse_equal(expected, result)

# check that index mismatches are correctly detected even if the `value`s
# have compatible shape
sp_incomp = sparse_ops.from_dense([[0.0, 1.0, 0.0], [-2.0, 0.0, 1.0]])
with self.assertRaises((errors.InvalidArgumentError, ValueError)):
    result = sparse_ops.map_values(mapping, sp, sp_incomp, kwarg='kwarg')
    self.evaluate(result)

# check that shape mismatches are correctly detected
sp_incomp = sparse_tensor.SparseTensor(sp.indices, sp.values, (25, 25))
with self.assertRaises((errors.InvalidArgumentError, ValueError)):
    result = sparse_ops.map_values(mapping, sp, sp_incomp, kwarg='kwarg')
    self.evaluate(result)
