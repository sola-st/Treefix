# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
node_name = "simple_mul_add/matmul"
tensor_name = node_name + ":0"
out = self._registry.dispatch_command(
    "print_tensor", [tensor_name, "-n", "1"], screen_info={"cols": 80})

self.assertEqual([
    "ERROR: Invalid number (1) for tensor simple_mul_add/matmul:0, "
    "which generated one dump."
], out.lines)

self.assertNotIn("tensor_metadata", out.annotations)

check_main_menu(
    self,
    out,
    list_tensors_enabled=True,
    node_info_node_name=node_name,
    list_inputs_node_name=node_name,
    list_outputs_node_name=node_name)
