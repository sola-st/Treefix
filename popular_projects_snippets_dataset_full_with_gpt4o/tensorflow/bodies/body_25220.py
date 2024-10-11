# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
self._debug_dump.set_python_graph(self._sess.graph)
out = self._registry.dispatch_command(
    "list_source", ["-p", self._curr_file_path, "-n", ".*read"])

self.assertEqual([
    "List of source files that created nodes in this run",
    "File path regex filter: \"%s\"" % self._curr_file_path,
    "Node name regex filter: \".*read\"", ""], out.lines[:4])
