# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
elem = CustomMap(foo=constant_op.constant(37.))
spec = structure.type_spec_from_value(elem)
self.assertIsInstance(spec, CustomMap)
self.assertEqual(spec["foo"], tensor_spec.TensorSpec([], dtypes.float32))
