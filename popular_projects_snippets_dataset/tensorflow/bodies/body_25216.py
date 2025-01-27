# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
self._debug_dump.set_python_graph(self._sess.graph)
out = self._registry.dispatch_command(
    "print_source",
    [self._curr_file_path, "-m", "1"],
    screen_info={"cols": 80})

index = self._findSourceLine(out, self._u_line_number)
self.assertEqual(
    ["L%d         u = variables.VariableV1(u_init, name=u_name)" %
     self._u_line_number,
     "    simple_mul_add/u",
     "    (... Omitted 2 of 3 op(s) ...) +5"],
    out.lines[index : index + 3])
self.assertEqual("pt simple_mul_add/u",
                 out.font_attr_segs[index + 1][0][2].content)
more_elements_command = out.font_attr_segs[index + 2][-1][2].content
self.assertStartsWith(more_elements_command,
                      "ps %s " % self._curr_file_path)
self.assertIn(" -m 6", more_elements_command)
