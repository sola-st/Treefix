# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
self._debug_dump.set_python_graph(self._sess.graph)
out = self._registry.dispatch_command(
    "print_source",
    [self._curr_file_path, "--tensors"],
    screen_info={"cols": 80})

# Verify the annotation of the line that creates u.
index = self._findSourceLine(out, self._u_line_number)
self.assertEqual(
    ["L%d         u = variables.VariableV1(u_init, name=u_name)" %
     self._u_line_number,
     "    simple_mul_add/u/read:0",
     "    simple_mul_add/u:0"],
    out.lines[index : index + 3])
self.assertEqual("pt simple_mul_add/u/read:0",
                 out.font_attr_segs[index + 1][0][2].content)
self.assertEqual("pt simple_mul_add/u:0",
                 out.font_attr_segs[index + 2][0][2].content)
