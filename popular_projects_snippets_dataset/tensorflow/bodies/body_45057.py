# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def test_fn(y):
    exit(y**2)

self.assertTrue(hasattr(api.to_graph(test_fn), 'ag_source_map'))
