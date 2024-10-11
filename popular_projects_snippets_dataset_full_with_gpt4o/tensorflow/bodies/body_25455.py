# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli_test.py
prof_output = self.prof_analyzer.print_source([
    __file__, "--init_line", str(self.loop_cond_lineno)])
self.assertEqual(
    self.loop_cond_lineno + 1,  # The extra line is due to the head lines.
    prof_output.annotations[debugger_cli_common.INIT_SCROLL_POS_KEY])
