# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py
func = lambda x: x + 10 if isinstance(x, int) else x
result = nest.map_structure_up_to(s1, func, s2, expand_composites=True)
self.assertEqual(result, expected)
