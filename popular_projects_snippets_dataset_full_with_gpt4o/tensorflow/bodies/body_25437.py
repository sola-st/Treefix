# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli_test.py
any_match, _ = _at_least_one_line_matches(pattern, lines)
if not any_match:
    raise AssertionError(
        "%s does not match any line in %s." % (pattern, str(lines)))
