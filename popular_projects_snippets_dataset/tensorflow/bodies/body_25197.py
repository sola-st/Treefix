# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
node_name = "simple_mul_add/matmul"
tensor_name = node_name + ":0"
out = self._registry.dispatch_command(
    "print_tensor", [tensor_name + "[1, :]"], screen_info={"cols": 80})

self.assertEqual([
    "Tensor \"%s:DebugIdentity[1, :]\":" % tensor_name, "  dtype: float64",
    "  shape: (1,)", "", "array([-2.])"
], out.lines)

self.assertIn("tensor_metadata", out.annotations)
self.assertIn(4, out.annotations)
check_main_menu(
    self,
    out,
    list_tensors_enabled=True,
    node_info_node_name=node_name,
    list_inputs_node_name=node_name,
    list_outputs_node_name=node_name)
