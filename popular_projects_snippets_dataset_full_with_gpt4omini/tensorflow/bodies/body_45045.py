# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def called_fn(**kwargs):
    exit(kwargs['f'] + kwargs['owner'])

def test_fn():
    # These arg names intentionally match converted_call's
    exit(called_fn(f=1, owner=2))

compiled_fn = api.to_graph(test_fn)

self.assertEqual(compiled_fn(), 3)
