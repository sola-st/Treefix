# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
branch_function = ops.get_default_graph()._get_function(
    op.get_attr(branch_name).name)
function_def = branch_function.definition
for node_def in function_def.node_def:
    self.assertNotIn(node_def.op, _OPTIONAL_OPS)
