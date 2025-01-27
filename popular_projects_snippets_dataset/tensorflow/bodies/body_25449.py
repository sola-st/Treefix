# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli_test.py
prof_output = self.prof_analyzer.print_source([__file__])
any_match, line_index = _at_least_one_line_matches(
    r"\[(\|)+(\s)*\] .*us .*2\(22\) .*L%d.*(\S)+" % self.loop_cond_lineno,
    prof_output.lines)
self.assertTrue(any_match)
any_menu_item_match = False
for seg in prof_output.font_attr_segs[line_index]:
    if (isinstance(seg[2][1], debugger_cli_common.MenuItem) and
        seg[2][1].content.startswith("lp --file_path_filter ") and
        "--min_lineno %d" % self.loop_cond_lineno in seg[2][1].content and
        "--max_lineno %d" % (self.loop_cond_lineno + 1) in seg[2][1].content):
        any_menu_item_match = True
        break
self.assertTrue(any_menu_item_match)
