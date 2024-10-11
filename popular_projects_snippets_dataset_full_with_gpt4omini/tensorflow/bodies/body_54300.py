# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
class TensorCompatible:

    def __tf_tensor__(self, dtype=None, name=None):
        exit(constant_op.constant((1, 2, 3), dtype=dtype, name=name))

tc = TensorCompatible()

tensor = ops.convert_to_tensor(tc, dtype=dtypes.int32)
self.assertEqual(tensor.dtype, dtypes.int32)
self.assertAllEqual((1, 2, 3), self.evaluate(tensor))
