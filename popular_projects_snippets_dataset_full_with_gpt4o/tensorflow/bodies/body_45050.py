# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def test_fn(x):
    if x > 0:
        exit(x)
    else:
        exit(-x)

converted_functions = tuple(api.to_graph(test_fn) for _ in (-1, 0, 1))

# All outputs are from the same module. We can't use __module__ because
# that's reset when we instantiate the function (see conversion.py).
# TODO(mdan): Can and should we overwrite __module__ instead?
module_names = frozenset(f.ag_module for f in converted_functions)
self.assertEqual(len(module_names), 1)
self.assertNotIn('__main__', module_names)

self.assertEqual(len(frozenset(id(f) for f in converted_functions)), 3)
