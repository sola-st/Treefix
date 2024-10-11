# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py
result = nest.flatten(structure, expand_composites=expand_composites)
self.assertEqual(result, expected)

result_with_paths = nest.flatten_with_tuple_paths(
    structure, expand_composites=expand_composites)
self.assertEqual(result_with_paths, list(zip(paths, expected)))

string_paths = ['/'.join(str(p) for p in path) for path in paths]  # pylint: disable=g-complex-comprehension
result_with_string_paths = nest.flatten_with_joined_string_paths(
    structure, expand_composites=expand_composites)
self.assertEqual(result_with_string_paths,
                 list(zip(string_paths, expected)))

flat_paths_result = list(
    nest.yield_flat_paths(structure, expand_composites=expand_composites))
self.assertEqual(flat_paths_result, paths)
