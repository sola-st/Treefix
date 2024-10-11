# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
fn = list_ops._build_element_shape
# Unknown shape -> -1.
self.assertEqual(fn(None), -1)
self.assertEqual(fn(tensor_shape.unknown_shape()), -1)
# Scalar shape -> [] with type int32.
self.assertEqual(fn([]).dtype, dtypes.int32)
self.assertEqual(fn(tensor_shape.TensorShape([])).dtype, dtypes.int32)
self.assertAllEqual(self.evaluate(fn([])), np.array([], np.int32))
self.assertAllEqual(
    self.evaluate(fn(tensor_shape.TensorShape([]))), np.array([], np.int32))
# Tensor -> Tensor
shape = constant_op.constant(1)
self.assertIs(fn(shape), shape)
# Shape with unknown dims -> shape list with -1's.
shape = [None, 5]
self.assertAllEqual(fn(shape), [-1, 5])
self.assertAllEqual(fn(tensor_shape.TensorShape(shape)), [-1, 5])
# Shape with unknown dims and tensor dims -> shape list with -1's and tensor
# dims.
t = array_ops.placeholder(dtypes.int32)
shape = [None, 5, t]
result = fn(shape)
self.assertAllEqual(result[:2], [-1, 5])
self.assertIs(result[2], t)
