# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
if not context.executing_eagerly():
    self.skipTest("Eager-mode test")
op = ops.Operation(
    ops._NodeDef("FloatOutput", "myop"), ops.Graph(), [], [dtypes.float32])
t = op.outputs[0]
with self.assertRaisesRegex(TypeError, "Cannot iterate"):
    iter(t)
