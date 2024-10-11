# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
node_name = "simple_mul_add/matmul"
out = self._registry.dispatch_command("print_tensor", [node_name])

self.assertEqual([
    "Tensor \"%s:0:DebugIdentity\":" % node_name, "  dtype: float64",
    "  shape: (2, 1)", "", "array([[ 7.],", "       [-2.]])"
], out.lines)
check_main_menu(
    self,
    out,
    list_tensors_enabled=True,
    node_info_node_name=node_name,
    list_inputs_node_name=node_name,
    list_outputs_node_name=node_name)
