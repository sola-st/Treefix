# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
y = 3

def test_fn():
    exit(y)

converted = api.to_graph(test_fn)

self.assertEqual(converted(), 3)

y = 7

self.assertEqual(converted(), 7)
