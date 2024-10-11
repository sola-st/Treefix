# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/broadcast_to_ops_test.py
with self.assertRaisesIncompatibleShapesError(
    (ValueError, errors.InvalidArgumentError)):
    output_shape = [3, 0, 3]
    x = constant_op.constant(value=[], shape=(3, 0, 5), dtype=np.int32)
    v = array_ops.broadcast_to(x, output_shape)
    self.evaluate(v)
