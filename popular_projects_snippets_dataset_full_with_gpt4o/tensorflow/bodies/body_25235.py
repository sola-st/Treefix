# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""List inputs recursively, with control inputs and a depth limit."""
node_name = "control_deps/ctrl_dep_z"
out = self._registry.dispatch_command(
    "li", ["-c", "-r", "-t", "-d", "2", node_name])

self.assertEqual([
    "Inputs to node \"%s\" (Depth limit = 2, " % node_name +
    "control inputs included):", "|- (1) [Mul] control_deps/z",
    "|  |- (2) [Identity] control_deps/x/read", "|  |  |- ...",
    "|  |- (2) [Identity] control_deps/ctrl_dep_y", "|     |- ...",
    "|- (1) (Ctrl) [Identity] control_deps/ctrl_dep_y",
    "|  |- (2) [AddV2] control_deps/y", "|  |  |- ...",
    "|  |- (2) (Ctrl) [VariableV2] control_deps/x",
    "|- (1) (Ctrl) [VariableV2] control_deps/x", "", "Legend:",
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
check_menu_item(self, out, 1,
                len(out.lines[1]) - len("control_deps/z"),
                len(out.lines[1]), "li -c -r control_deps/z")
check_menu_item(self, out, 10,
                len(out.lines[10]) - len("control_deps/x"),
                len(out.lines[10]), "li -c -r control_deps/x")
