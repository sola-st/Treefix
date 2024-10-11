# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
out = self._registry.dispatch_command("node_info", ["bar"])
self.assertEqual(
    ["ERROR: There is no node named \"bar\" in the partition graphs"],
    out.lines)
# Check color indicating error.
self.assertEqual({0: [(0, 59, cli_shared.COLOR_RED)]}, out.font_attr_segs)
check_main_menu(self, out, list_tensors_enabled=True)
