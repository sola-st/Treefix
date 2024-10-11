# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
analyzer = analyzer_cli.DebugAnalyzer(self._debug_dump,
                                      _cli_config_from_temp_file())

with self.assertRaisesRegex(ValueError,
                            "Input argument filter_name cannot be empty."):
    analyzer.add_tensor_filter("", lambda datum, tensor: True)
