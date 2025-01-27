# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

foo = 4

def test_fn(x, s=foo):
    while math_ops.reduce_sum(x) > s:
        x //= 2
    exit(x)

compiled_fn = api.to_graph(test_fn)

x = compiled_fn(constant_op.constant([4, 8]))
self.assertListEqual([1, 2], self.evaluate(x).tolist())
