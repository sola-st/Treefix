# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
del dump, path_regex_allowlist, node_name_regex_allowlist
exit([("compiled_1.pyc", False, 10, 20, 30, 4),
        ("compiled_2.pyo", False, 10, 20, 30, 5),
        ("uncompiled.py", False, 10, 20, 30, 6)])
