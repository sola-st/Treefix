# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py
func = lambda x: x + 10
result = nest.map_structure(
    func, structure, expand_composites=expand_composites)
self.assertEqual(result, expected)
