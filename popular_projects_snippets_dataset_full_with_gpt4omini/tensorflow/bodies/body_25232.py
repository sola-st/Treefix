# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""List inputs using the name of an output tensor of the node."""

# Do not include node op types.
node_name = "control_deps/z"
tensor_name = node_name + ":0"
out = self._registry.dispatch_command("list_inputs", [tensor_name])

self.assertEqual([
    "Inputs to node \"%s\" (Depth limit = 1):" % node_name,
    "|- (1) control_deps/x/read", "|  |- ...",
    "|- (1) control_deps/ctrl_dep_y", "   |- ...", "", "Legend:",
    "  (d): recursion depth = d."
], out.lines)
check_main_menu(
    self,
    out,
    list_tensors_enabled=True,
    node_info_node_name=node_name,
    print_tensor_node_name=node_name,
    list_outputs_node_name=node_name)
check_menu_item(self, out, 1,
                len(out.lines[1]) - len("control_deps/x/read"),
                len(out.lines[1]), "li -c -r control_deps/x/read")
check_menu_item(self, out, 3,
                len(out.lines[3]) - len("control_deps/ctrl_dep_y"),
                len(out.lines[3]), "li -c -r control_deps/ctrl_dep_y")
