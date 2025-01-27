# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
# Call node_info on a node with control inputs.
out = self._registry.dispatch_command("node_info",
                                      ["control_deps/ctrl_dep_y"])

assert_node_attribute_lines(self, out, "control_deps/ctrl_dep_y",
                            "Identity", self._main_device,
                            [("AddV2", "control_deps/y")],
                            [("VariableV2", "control_deps/x")],
                            [("Mul", "control_deps/z")],
                            [("Identity", "control_deps/ctrl_dep_z")])

# Call node info on a node with control recipients.
out = self._registry.dispatch_command("ni", ["control_deps/x"])

assert_node_attribute_lines(self, out, "control_deps/x", "VariableV2",
                            self._main_device, [], [],
                            [("Identity", "control_deps/x/read")],
                            [("Identity", "control_deps/ctrl_dep_y"),
                             ("Identity", "control_deps/ctrl_dep_z")])

# Verify the menu items (command shortcuts) in the output.
check_menu_item(self, out, 10,
                len(out.lines[10]) - len("control_deps/x/read"),
                len(out.lines[10]), "ni -a -d -t control_deps/x/read")
if out.lines[13].endswith("control_deps/ctrl_dep_y"):
    y_line = 13
    z_line = 14
else:
    y_line = 14
    z_line = 13
check_menu_item(self, out, y_line,
                len(out.lines[y_line]) - len("control_deps/ctrl_dep_y"),
                len(out.lines[y_line]),
                "ni -a -d -t control_deps/ctrl_dep_y")
check_menu_item(self, out, z_line,
                len(out.lines[z_line]) - len("control_deps/ctrl_dep_z"),
                len(out.lines[z_line]),
                "ni -a -d -t control_deps/ctrl_dep_z")
