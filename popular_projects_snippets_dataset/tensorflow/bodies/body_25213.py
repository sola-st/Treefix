# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
self._debug_dump.set_python_graph(self._sess.graph)
out = self._registry.dispatch_command(
    "print_source", [self._curr_file_path], screen_info={"cols": 80})

# Verify the annotation of the line that creates u.
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

# Verify the annotation of the line that creates v.
index = self._findSourceLine(out, self._v_line_number)
self.assertEqual(
    ["L%d         v = variables.VariableV1(v_init, name=v_name)" %
     self._v_line_number,
     "    simple_mul_add/v"],
    out.lines[index : index + 2])
self.assertEqual("pt simple_mul_add/v",
                 out.font_attr_segs[index + 1][0][2].content)

# Verify the annotation of the line that creates w.
index = self._findSourceLine(out, self._w_line_number)
self.assertEqual(
    ["L%d         " % self._w_line_number +
     "w = math_ops.matmul(u, v, name=\"simple_mul_add/matmul\")",
     "    simple_mul_add/matmul"],
    out.lines[index : index + 2])
self.assertEqual("pt simple_mul_add/matmul",
                 out.font_attr_segs[index + 1][0][2].content)

# Verify the annotation of the line that creates x.
index = self._findSourceLine(out, self._x_line_number)
self.assertEqual(
    ["L%d         " % self._x_line_number +
     "x = math_ops.add(w, w, name=\"simple_mul_add/add\")",
     "    simple_mul_add/add"],
    out.lines[index : index + 2])
self.assertEqual("pt simple_mul_add/add",
                 out.font_attr_segs[index + 1][0][2].content)
