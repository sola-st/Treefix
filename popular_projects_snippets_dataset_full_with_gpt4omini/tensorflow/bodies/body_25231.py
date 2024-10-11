# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""List inputs non-recursively, without any control inputs."""

# Do not include node op types.
node_name = "control_deps/z"
out = self._registry.dispatch_command("list_inputs", [node_name])

self.assertEqual([
    "Inputs to node \"%s\" (Depth limit = 1):" % node_name,
    "|- (1) control_deps/x/read", "|  |- ...",
    "|- (1) control_deps/ctrl_dep_y", "   |- ...", "", "Legend:",
    "  (d): recursion depth = d."
], out.lines)

# Include node op types.
out = self._registry.dispatch_command("li", ["-t", node_name])

self.assertEqual([
    "Inputs to node \"%s\" (Depth limit = 1):" % node_name,
    "|- (1) [Identity] control_deps/x/read", "|  |- ...",
    "|- (1) [Identity] control_deps/ctrl_dep_y", "   |- ...", "", "Legend:",
    "  (d): recursion depth = d.", "  [Op]: Input node has op type Op."
], out.lines)
check_main_menu(
    self,
    out,
    list_tensors_enabled=True,
    node_info_node_name=node_name,
    print_tensor_node_name=node_name,
    list_outputs_node_name=node_name)

# Verify that the node name has bold attribute.
self.assertEqual([(16, 16 + len(node_name), "bold")], out.font_attr_segs[0])

# Verify the menu items (command shortcuts) in the output.
check_menu_item(self, out, 1,
                len(out.lines[1]) - len("control_deps/x/read"),
                len(out.lines[1]), "li -c -r control_deps/x/read")
check_menu_item(self, out, 3,
                len(out.lines[3]) - len("control_deps/ctrl_dep_y"),
                len(out.lines[3]), "li -c -r control_deps/ctrl_dep_y")
