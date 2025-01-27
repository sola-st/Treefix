# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
node_name = "simple_mul_add/u/read"
tensor_name = node_name + ":0"
out = self._registry.dispatch_command("node_info", [tensor_name])

assert_node_attribute_lines(self, out, node_name, "Identity",
                            self._main_device,
                            [("VariableV2", "simple_mul_add/u")], [],
                            [(_matmul_op_name(), "simple_mul_add/matmul")],
                            [])
check_main_menu(
    self,
    out,
    list_tensors_enabled=True,
    list_inputs_node_name=node_name,
    print_tensor_node_name=node_name,
    list_outputs_node_name=node_name)
