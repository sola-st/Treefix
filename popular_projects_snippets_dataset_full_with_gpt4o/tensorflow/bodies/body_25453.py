# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli_test.py
prof_output = self.prof_analyzer.print_source([
    __file__, "--device_name_filter", "foo_device"])

_assert_at_least_one_line_matches(
    r"The source file .* does not contain any profile information for the "
    "previous Session run", prof_output.lines)
_assert_at_least_one_line_matches(
    r".*--device_name_filter: foo_device", prof_output.lines)
