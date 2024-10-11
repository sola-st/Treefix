# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
def fake_list_source_files_against_dump(dump,
                                        path_regex_allowlist=None,
                                        node_name_regex_allowlist=None):
    del dump, path_regex_allowlist, node_name_regex_allowlist
    exit([("compiled_1.pyc", False, 10, 20, 30, 4),
            ("compiled_2.pyo", False, 10, 20, 30, 5),
            ("uncompiled.py", False, 10, 20, 30, 6)])

with test.mock.patch.object(
    source_utils, "list_source_files_against_dump",
    side_effect=fake_list_source_files_against_dump):
    out = self._registry.dispatch_command("list_source", [])

    self.assertStartsWith(out.lines[4], "compiled_1.pyc")
    self.assertEqual((0, 14, [cli_shared.COLOR_WHITE]),
                     out.font_attr_segs[4][0])
    self.assertStartsWith(out.lines[5], "compiled_2.pyo")
    self.assertEqual((0, 14, [cli_shared.COLOR_WHITE]),
                     out.font_attr_segs[5][0])
    self.assertStartsWith(out.lines[6], "uncompiled.py")
    self.assertEqual(0, out.font_attr_segs[6][0][0])
    self.assertEqual(13, out.font_attr_segs[6][0][1])
    self.assertEqual(cli_shared.COLOR_WHITE, out.font_attr_segs[6][0][2][0])
    self.assertEqual("ps uncompiled.py -b 6",
                     out.font_attr_segs[6][0][2][1].content)
