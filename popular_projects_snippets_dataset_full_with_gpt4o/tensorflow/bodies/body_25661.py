# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
self._tc_reg = debugger_cli_common.TabCompletionRegistry()

# Register the items in an unsorted order deliberately, to test the sorted
# output from get_completions().
self._tc_reg.register_tab_comp_context(
    ["print_tensor", "pt"],
    ["node_b:1", "node_b:2", "node_a:1", "node_a:2"])
self._tc_reg.register_tab_comp_context(["node_info"],
                                       ["node_c", "node_b", "node_a"])
