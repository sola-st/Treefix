# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
op = ops.Operation(
    ops._NodeDef("FloatOutput", "myop"), ops.Graph(), [], [dtypes.bool])
t = op.outputs[0]
with self.assertRaisesRegex(TypeError,
                            "Using.*as a.*bool.*not allowed in Graph"):
    bool(t)
with self.assertRaisesRegex(TypeError,
                            "Using.*as a.*bool.*AutoGraph did convert"):
    with ag_ctx.ControlStatusCtx(ag_ctx.Status.ENABLED):
        bool(t)
with self.assertRaisesRegex(TypeError,
                            "Using.*as a.*bool.*AutoGraph is disabled"):
    with ag_ctx.ControlStatusCtx(ag_ctx.Status.DISABLED):
        bool(t)
