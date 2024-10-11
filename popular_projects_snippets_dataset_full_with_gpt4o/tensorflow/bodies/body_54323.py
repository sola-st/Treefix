# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
op1 = g.create_op(
    "RefOutputFloatOutput", [], [dtypes.float32_ref, dtypes.float32],
    name="op1")
self.assertProtoEquals("op:'RefOutputFloatOutput' name:'op1'", op1.node_def)
ref_t, nonref_t = op1.values()
# NOTE(mrry): Must specify input_types to preserve ref-typed input.
op2 = g.create_op(
    "RefInputFloatInput", [ref_t, nonref_t], [],
    input_types=[dtypes.float32_ref, dtypes.float32],
    name="op2")
self.assertProtoEquals(
    "op:'RefInputFloatInput' name:'op2' input:'op1' input:'op1:1'",
    op2.node_def)
op3 = g.create_op("TwoFloatInputs", [ref_t, nonref_t], [], name="op3")
self.assertProtoEquals(
    "op:'TwoFloatInputs' name:'op3' input:'op1' input:'op1:1'",
    op3.node_def)
