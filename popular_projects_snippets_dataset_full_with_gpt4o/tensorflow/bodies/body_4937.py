# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
v = variables_lib.Variable(array_ops.zeros((30, 1)))
# Make sure values does not contain 0 due to testing `scatter_div`!
sparse_delta = indexed_slices.IndexedSlices(
    values=constant_op.constant([[1.], [2.], [3.], [4.], [5.]]),
    indices=constant_op.constant([0, 10, 12, 21, 22]))

v0 = variables_lib.Variable(array_ops.zeros((10, 1)))
v1 = variables_lib.Variable(array_ops.zeros((10, 1)))
v2 = variables_lib.Variable(array_ops.zeros((10, 1)))
sv = sharded_variable.ShardedVariable([v0, v1, v2])

getattr(v, op)(sparse_delta, name='scatter_v')
getattr(sv, op)(sparse_delta, name='scatter_sv')
self.assertAllEqual(v, ops.convert_to_tensor(sv))

@def_function.function
def func():
    getattr(v, op)(sparse_delta, name='scatter_v')
    getattr(sv, op)(sparse_delta, name='scatter_sv')

func()
self.assertAllEqual(v, ops.convert_to_tensor(sv))
