# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
tst.assertFalse(reverse and "-r" in command)
tst.assertFalse(not(op_type_regex) and ("-t %s" % op_type_regex) in command)
tst.assertFalse(
    not(node_name_regex) and ("-t %s" % node_name_regex) in command)
tst.assertFalse(
    not(tensor_filter_name) and ("-t %s" % tensor_filter_name) in command)
