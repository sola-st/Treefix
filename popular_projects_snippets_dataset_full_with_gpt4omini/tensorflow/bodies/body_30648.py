# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
shape = (10, 10)
init = init_ops.identity_initializer()
partitioner = partitioned_variables.variable_axis_size_partitioner(1)
with self.session(graph=ops.Graph(), use_gpu=True):
    with variable_scope.variable_scope(
        "foo", partitioner=partitioner, initializer=init):
        v = array_ops.identity(variable_scope.get_variable("bar", shape=shape))
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose(v, np.eye(*shape))
