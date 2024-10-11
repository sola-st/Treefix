# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
node_def = ops._NodeDef("None", "op1")
op = ops.Operation(node_def, ops.Graph(), [], [dtypes.float32])
self.assertEqual(str(node_def), str(op))
