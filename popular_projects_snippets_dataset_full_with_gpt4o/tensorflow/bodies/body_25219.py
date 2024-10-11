# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
self._debug_dump.set_python_graph(self._sess.graph)
out = self._registry.dispatch_command("list_source", ["-n", "^$"])

self.assertEqual([
    "List of source files that created nodes in this run",
    "Node name regex filter: \"^$\"", "",
    "[No source file information.]"], out.lines)
