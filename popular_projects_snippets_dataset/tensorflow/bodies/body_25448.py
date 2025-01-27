# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli_test.py
prof_output = self.prof_analyzer.print_source([__file__])

_assert_at_least_one_line_matches(
    r"\[(\|)+(\s)*\] .*us .*2\(22\) .*L%d.*(\S)+" % self.loop_cond_lineno,
    prof_output.lines)
_assert_at_least_one_line_matches(
    r"\[(\|)+(\s)*\] .*us .*2\(20\) .*L%d.*(\S)+" % self.loop_body_lineno,
    prof_output.lines)
_assert_at_least_one_line_matches(
    r"\[(\|)+(\s)*\] .*us .*7\(55\) .*L%d.*(\S)+" % self.loop_lineno,
    prof_output.lines)
