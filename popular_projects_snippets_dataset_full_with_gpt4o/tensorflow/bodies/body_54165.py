# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py
func = lambda t: not (isinstance(t, CT) and t.metadata == 'B')
structure = [CT([1, 2], metadata='A'), CT([CT(3)], metadata='B')]

result = nest.get_traverse_shallow_structure(
    func, structure, expand_composites=True)
expected = [CT([True, True], metadata='A'), False]
self.assertEqual(result, expected)
