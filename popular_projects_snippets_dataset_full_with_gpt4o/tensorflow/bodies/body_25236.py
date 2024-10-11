# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""List the inputs to a node without any input."""
node_name = "control_deps/x"
out = self._registry.dispatch_command("li", ["-c", "-r", "-t", node_name])

self.assertEqual([
    "Inputs to node \"%s\" (Depth limit = 20, control " % node_name +
    "inputs included):", "  [None]", "", "Legend:",
    "  (d): recursion depth = d.", "  (Ctrl): Control input.",
    "  [Op]: Input node has op type Op."
], out.lines)
check_main_menu(
    self,
    out,
    list_tensors_enabled=True,
    node_info_node_name=node_name,
    print_tensor_node_name=node_name,
    list_outputs_node_name=node_name)
