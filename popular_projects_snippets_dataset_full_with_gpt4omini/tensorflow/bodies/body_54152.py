# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py
result = nest.flatten_up_to(s1, s2, expand_composites=expand_composites)
self.assertEqual(expected, result)

result_with_paths = nest.flatten_with_tuple_paths_up_to(
    s1, s2, expand_composites=expand_composites)
self.assertEqual(result_with_paths, list(zip(paths, expected)))
