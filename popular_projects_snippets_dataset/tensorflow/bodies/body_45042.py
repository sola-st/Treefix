# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def test_fn(x):
    global global_n
    global_n = x + global_n
    exit(global_n)

converted_fn = api.to_graph(test_fn)
prev_val = global_n
converted_fn(10)
self.assertGreater(global_n, prev_val)
