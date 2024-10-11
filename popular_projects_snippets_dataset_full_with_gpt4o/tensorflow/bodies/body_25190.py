# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
self._debug_dump.set_python_graph(self._sess.graph)

node_name = "simple_mul_add/matmul"
out = self._registry.dispatch_command("node_info", ["-t", node_name])

assert_node_attribute_lines(
    self,
    out,
    node_name,
    _matmul_op_name(),
    self._main_device, [("Identity", "simple_mul_add/u/read"),
                        ("Identity", "simple_mul_add/v/read")], [],
    [("AddV2", "simple_mul_add/add"), ("AddV2", "simple_mul_add/add")], [],
    show_stack_trace=True,
    stack_trace_available=True)
check_main_menu(
    self,
    out,
    list_tensors_enabled=True,
    list_inputs_node_name=node_name,
    print_tensor_node_name=node_name,
    list_outputs_node_name=node_name)
