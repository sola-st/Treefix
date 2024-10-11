# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
ref_t, nonref_t = _apply_op(
    g, "RefOutputFloatOutput", [], [dtypes.float32_ref, dtypes.float32],
    name="op1")
self.assertProtoEquals("op:'RefOutputFloatOutput' name:'op1'",
                       ref_t.op.node_def)
# NOTE(mrry): Must specify input_types to preserve ref-typed input.
out_2 = _apply_op(
    g,
    "RefInputFloatInputIntOutput", [ref_t, nonref_t], [dtypes.int32],
    input_types=[dtypes.float32_ref, dtypes.float32],
    name="op2")
self.assertProtoEquals(
    "op:'RefInputFloatInputIntOutput' name:'op2' input:'op1' input:'op1:1'",
    out_2.op.node_def)
out_3 = _apply_op(
    g, "TwoFloatInputsIntOutput", [ref_t, nonref_t], [dtypes.int32],
    name="op3")
self.assertProtoEquals(
    "op:'TwoFloatInputsIntOutput' name:'op3' input:'op1' input:'op1:1'",
    out_3.op.node_def)
