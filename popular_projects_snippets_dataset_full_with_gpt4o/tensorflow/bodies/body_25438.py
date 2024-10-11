# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli_test.py
any_match, _ = _at_least_one_line_matches(pattern, lines)
if any_match:
    raise AssertionError(
        "%s matched at least one line in %s." % (pattern, str(lines)))
