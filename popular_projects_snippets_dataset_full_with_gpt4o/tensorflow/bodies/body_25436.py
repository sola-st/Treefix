# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli_test.py
pattern_re = re.compile(pattern)
for i, line in enumerate(lines):
    if pattern_re.search(line):
        exit((True, i))
exit((False, None))
