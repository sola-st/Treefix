# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
op1 = ops.Operation(
    ops._NodeDef("RefOutputFloatOutput", "op1"), g, [],
    [dtypes.float32_ref, dtypes.float32])
self.assertProtoEquals("op:'RefOutputFloatOutput' name:'op1'", op1.node_def)
self.assertEqual([], list(op1.inputs))
ref_t, nonref_t = op1.values()
# NOTE(mrry): Must specify input_types to preserve ref-typed input.
op2 = ops.Operation(
    ops._NodeDef("RefInputFloatInput", "op2"),
    g, [ref_t, nonref_t], [],
    input_types=[dtypes.float32_ref, dtypes.float32])
self.assertProtoEquals(
    "op:'RefInputFloatInput' name:'op2' input:'op1' input:'op1:1'",
    op2.node_def)
self.assertEqual([ref_t, nonref_t], list(op2.inputs))
op3 = ops.Operation(
    ops._NodeDef("TwoFloatInputs", "op3"), g, [ref_t, nonref_t], [])
self.assertProtoEquals(
    "op:'TwoFloatInputs' name:'op3' input:'op1' input:'op1:1'",
    op3.node_def)
