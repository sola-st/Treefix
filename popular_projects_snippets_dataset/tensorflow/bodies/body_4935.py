# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
v = variables_lib.Variable(array_ops.zeros((32, 1)))
sparse_delta = indexed_slices.IndexedSlices(
    values=constant_op.constant([[0.], [1.], [2.], [3.], [4.], [5.]]),
    indices=constant_op.constant([0, 10, 11, 12, 30, 31]))

v0 = variables_lib.Variable(array_ops.zeros((11, 1)))
v1 = variables_lib.Variable(array_ops.zeros((11, 1)))
v2 = variables_lib.Variable(array_ops.zeros((10, 1)))
sv = sharded_variable.ShardedVariable([v0, v1, v2])

v.scatter_add(sparse_delta)
sv.scatter_add(sparse_delta)
self.assertAllEqual(v, ops.convert_to_tensor(sv))

@def_function.function
def func():
    v.scatter_add(sparse_delta)
    sv.scatter_add(sparse_delta)

func()
self.assertAllEqual(v, ops.convert_to_tensor(sv))
