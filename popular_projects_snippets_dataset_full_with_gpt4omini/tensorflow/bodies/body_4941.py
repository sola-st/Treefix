# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
v = variables_lib.Variable(array_ops.zeros((30, 1)))
indices = constant_op.constant([0, 10, 12, 21, 22])

v0 = variables_lib.Variable(array_ops.zeros((10, 1)))
v1 = variables_lib.Variable(array_ops.zeros((10, 1)))
v2 = variables_lib.Variable(array_ops.zeros((10, 1)))
sv = sharded_variable.ShardedVariable([v0, v1, v2])

self.assertAllEqual(v.sparse_read(indices), sv.sparse_read(indices))

@def_function.function
def func():
    exit((v.sparse_read(indices), sv.sparse_read(indices)))

got, expect = func()
self.assertAllEqual(got, expect)
