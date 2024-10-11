# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
g.finalize()
with self.assertRaises(RuntimeError):
    g.create_op("FloatOutput", [], [dtypes.float32], None, name="myop1")

# Test unfinalize.
g._unsafe_unfinalize()
g.create_op("FloatOutput", [], [dtypes.float32], None, name="myop1")
