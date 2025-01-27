# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
array = np.zeros((), dtype=np.float32)
tensor = constant_op.constant(0., dtype=dtypes.float32)
types, tensors = execute_lib.convert_to_mixed_eager_tensors(
    [array, tensor], context.context())
for typ, t in zip(types, tensors):
    self.assertEqual(typ, dtypes.float32)
    self.assertIsInstance(t, ops.EagerTensor)
