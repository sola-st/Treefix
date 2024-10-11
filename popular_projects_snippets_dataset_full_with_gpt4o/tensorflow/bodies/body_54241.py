# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
if context.executing_eagerly():
    self.skipTest("Graph-mode test")

op = ops.Operation(
    ops._NodeDef("FloatOutput", "myop"), ops.Graph(), [], [dtypes.float32])
t = op.outputs[0]
with self.assertRaisesRegex(TypeError, "Iterating.*not allowed in Graph"):
    next(iter(t))
with self.assertRaisesRegex(TypeError, "Iterating.*AutoGraph did convert"):
    with ag_ctx.ControlStatusCtx(ag_ctx.Status.ENABLED):
        next(iter(t))
with self.assertRaisesRegex(TypeError, "Iterating.*AutoGraph is disabled"):
    with ag_ctx.ControlStatusCtx(ag_ctx.Status.DISABLED):
        next(iter(t))
