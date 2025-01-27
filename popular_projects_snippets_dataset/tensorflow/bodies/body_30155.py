# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
var2 = variables.Variable(
    array_ops.reshape(
        math_ops.cast(math_ops.range(1, 5, 1), dtypes.float32),
        shape=(4, 1, 1)))
varshape = variables.Variable([6, 4, 4], dtype=dtypes.int32)
begin = constant_op.constant([0, 0, 0])
end = constant_op.constant([4, 1, 1])
strides = constant_op.constant([1, 1, 1])
foo = array_ops.strided_slice_grad(varshape, begin, end, strides, var2)
self.evaluate(var2.initializer)
self.evaluate(varshape.initializer)
self.evaluate(foo)
