# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
self._debug_dump.set_python_graph(self._sess.graph)
out = self._registry.dispatch_command("list_source", ["-n", ".*/read"])

self.assertStartsWith(out.lines[1], "Node name regex filter: \".*/read\"")

non_tf_lib_files_start = [
    i for i in range(len(out.lines))
    if out.lines[i].startswith("Source file path")
][0] + 1
non_tf_lib_files_end = [
    i for i in range(len(out.lines))
    if out.lines[i].startswith("TensorFlow Python library file(s):")
][0] - 1
non_tf_lib_files = [
    line.split(" ")[0] for line
    in out.lines[non_tf_lib_files_start : non_tf_lib_files_end]]
self.assertIn(self._curr_file_path, non_tf_lib_files)

# Check that the TF library files are marked with special color attribute.
for i in range(non_tf_lib_files_end + 1, len(out.lines)):
    if not out.lines[i]:
        continue
    for attr_seg in  out.font_attr_segs[i]:
        self.assertTrue(cli_shared.COLOR_GRAY in attr_seg[2] or
                        attr_seg[2] == cli_shared.COLOR_GRAY)
