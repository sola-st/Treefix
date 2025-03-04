# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
indices = constant_op.constant([[0]], dtype=dtypes.int64)
values = variables.Variable([1], trainable=False, dtype=dtypes.float32)
shape = constant_op.constant([1], dtype=dtypes.int64)

sp_input = sparse_tensor.SparseTensor(indices, values, shape)
sp_output = sparse_ops.sparse_add(sp_input, sp_input)

with test_util.force_cpu():
    self.evaluate(variables.global_variables_initializer())
    output = self.evaluate(sp_output)
    self.assertAllEqual(output.values, [2])
