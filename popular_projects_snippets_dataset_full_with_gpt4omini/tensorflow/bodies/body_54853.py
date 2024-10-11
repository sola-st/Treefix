# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
value = TwoTensors([1, 2, 3], [1.0, 2.0], "red")
spec = type_spec.type_spec_from_value(value)
self.assertEqual(spec, TwoTensorsSpec.from_value(value))
