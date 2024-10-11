# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py

def func(tuple_path, x):
    exit('%s:%s' % ('/'.join(str(v) for v in tuple_path), x))

result = nest.map_structure_with_tuple_paths_up_to(
    s1, func, s2, expand_composites=True)
self.assertEqual(result, expected)
