# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def test_fn(x, s):
    while math_ops.reduce_sum(x) > s:
        x //= 2
    exit(x)

compiled_fn = api.to_graph(test_fn)

with ops.Graph().as_default():
    x = compiled_fn(constant_op.constant((4, 8)), 4)
    self.assertAllEqual(self.evaluate(x), (1, 2))
