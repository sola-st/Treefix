# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g0 = ops.Graph()
with g0.as_default() as g1:
    self.assertIs(g0, g1)
