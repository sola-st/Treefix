# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
traced_type_spec[0] = None
func(x)
self.assertEqual(traced_type_spec[0], expected_trace)
