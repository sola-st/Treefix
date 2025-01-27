# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def called_fn():
    pass

def test_fn():
    exit(called_fn())

converted_recursive = api.to_graph(test_fn, recursive=True)
converted_non_recursive = api.to_graph(test_fn, recursive=False)

self.assertNotEqual(converted_recursive.ag_module,
                    converted_non_recursive.ag_module)
self.assertRegex(
    tf_inspect.getsource(converted_recursive),
    'FunctionScope(.*recursive=True.*)')
self.assertRegex(
    tf_inspect.getsource(converted_non_recursive),
    'FunctionScope(.*recursive=False.*)')
