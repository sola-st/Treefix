# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
self._debug_dump.set_python_graph(self._sess.graph)
out = self._registry.dispatch_command(
    "print_source",
    [self._curr_file_path, "-b", "3"],
    screen_info={"cols": 80})

self.assertEqual(
    2, out.annotations[debugger_cli_common.INIT_SCROLL_POS_KEY])

index = self._findSourceLine(out, self._u_line_number)
self.assertEqual(
    ["L%d         u = variables.VariableV1(u_init, name=u_name)" %
     self._u_line_number,
     "    simple_mul_add/u",
     "    simple_mul_add/u/Assign",
     "    simple_mul_add/u/read"],
    out.lines[index : index + 4])
self.assertEqual("pt simple_mul_add/u",
                 out.font_attr_segs[index + 1][0][2].content)
# simple_mul_add/u/Assign is not used in this run because the Variable has
# already been initialized.
self.assertEqual(cli_shared.COLOR_BLUE, out.font_attr_segs[index + 2][0][2])
self.assertEqual("pt simple_mul_add/u/read",
                 out.font_attr_segs[index + 3][0][2].content)
