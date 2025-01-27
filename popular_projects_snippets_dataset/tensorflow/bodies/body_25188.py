# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
node_name = "simple_mul_add/matmul"
out = self._registry.dispatch_command("node_info", ["-d", node_name])

assert_node_attribute_lines(
    self,
    out,
    node_name,
    _matmul_op_name(),
    self._main_device, [("Identity", "simple_mul_add/u/read"),
                        ("Identity", "simple_mul_add/v/read")], [],
    [("AddV2", "simple_mul_add/add"), ("AddV2", "simple_mul_add/add")], [],
    num_dumped_tensors=1)
check_main_menu(
    self,
    out,
    list_tensors_enabled=True,
    list_inputs_node_name=node_name,
    print_tensor_node_name=node_name,
    list_outputs_node_name=node_name)
check_menu_item(self, out, 16,
                len(out.lines[16]) - len(out.lines[16].strip()),
                len(out.lines[16]), "pt %s:0 -n 0" % node_name)
