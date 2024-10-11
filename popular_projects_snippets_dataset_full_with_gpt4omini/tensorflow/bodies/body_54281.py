# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
op1 = ops.Operation(
    ops._NodeDef("None", "op1"), g, [],
    [dtypes.float32_ref, dtypes.float32])
self.assertIn("testTraceback", op1.traceback[-1])
