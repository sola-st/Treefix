# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
with self.assertRaisesRegex(KeyError,
                            "Context word \"foo\" has not been registered"):
    self._tc_reg.remove_comp_items("foo", ["node_a:1", "node_a:2"])
