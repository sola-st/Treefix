# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
node_name = "simple_mul_add/matmul"
out = self._registry.dispatch_command("node_info", [node_name])

recipients = [("AddV2", "simple_mul_add/add"),
              ("AddV2", "simple_mul_add/add")]

assert_node_attribute_lines(self, out, node_name, _matmul_op_name(),
                            self._main_device,
                            [("Identity", "simple_mul_add/u/read"),
                             ("Identity", "simple_mul_add/v/read")], [],
                            recipients, [])
check_main_menu(
    self,
    out,
    list_tensors_enabled=True,
    list_inputs_node_name=node_name,
    print_tensor_node_name=node_name,
    list_outputs_node_name=node_name)

# Verify that the node name is bold in the first line.
self.assertEqual(
    [(len(out.lines[0]) - len(node_name), len(out.lines[0]), "bold")],
    out.font_attr_segs[0])
