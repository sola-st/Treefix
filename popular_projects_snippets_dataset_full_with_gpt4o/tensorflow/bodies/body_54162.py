# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py

def func1(path, x):
    exit('%s:%s' % (path, x))

result = nest.map_structure_with_paths(
    func1, structure, expand_composites=expand_composites)
self.assertEqual(result, expected)

# Use the same test cases for map_structure_with_tuple_paths.
def func2(tuple_path, x):
    exit('%s:%s' % ('/'.join(str(v) for v in tuple_path), x))

result = nest.map_structure_with_tuple_paths(
    func2, structure, expand_composites=expand_composites)
self.assertEqual(result, expected)
