# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
if isinstance(rt, list):
    rt = ragged_factory_ops.constant(rt, dtype=dtypes.int32)
else:
    rt = ragged_tensor.convert_to_tensor_or_ragged_tensor(rt)
if context.executing_eagerly():
    actual = rt.numpy()
    self.assertNumpyObjectTensorsRecursivelyEqual(
        expected, actual, 'Expected %r, got %r' % (expected, actual))
else:
    with self.assertRaisesRegex(ValueError, 'only supported in eager mode'):
        rt.numpy()
