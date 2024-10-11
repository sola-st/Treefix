# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""List recipients recursively, with control inputs and a depth limit."""

out = self._registry.dispatch_command(
    "lo", ["-c", "-r", "-t", "-d", "1", "control_deps/x"])

self.assertEqual([
    "Recipients of node \"control_deps/x\" (Depth limit = 1, control "
    "recipients included):",
    "|- (1) [Identity] control_deps/x/read",
    "|  |- ...",
    "|- (1) (Ctrl) [Identity] control_deps/ctrl_dep_y",
    "|  |- ...",
    "|- (1) (Ctrl) [Identity] control_deps/ctrl_dep_z",
    "", "Legend:", "  (d): recursion depth = d.",
    "  (Ctrl): Control input.",
    "  [Op]: Input node has op type Op."], out.lines)
check_menu_item(self, out, 1,
                len(out.lines[1]) - len("control_deps/x/read"),
                len(out.lines[1]), "lo -c -r control_deps/x/read")
check_menu_item(self, out, 3,
                len(out.lines[3]) - len("control_deps/ctrl_dep_y"),
                len(out.lines[3]), "lo -c -r control_deps/ctrl_dep_y")
check_menu_item(self, out, 5,
                len(out.lines[5]) - len("control_deps/ctrl_dep_z"),
                len(out.lines[5]), "lo -c -r control_deps/ctrl_dep_z")

# Verify the bold attribute of the node name.
self.assertEqual([(20, 20 + len("control_deps/x"), "bold")],
                 out.font_attr_segs[0])
