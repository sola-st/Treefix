# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
with self.assertRaisesRegex(KeyError,
                            "Context word \"foo\" has not been registered"):
    self._tc_reg.extend_comp_items("foo", ["node_A:1", "node_A:2"])
