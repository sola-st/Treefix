# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
analyzer = analyzer_cli.DebugAnalyzer(self._debug_dump,
                                      _cli_config_from_temp_file())

with self.assertRaisesRegex(
    TypeError, "Input argument filter_name is expected to be str, "
    "but is not"):
    analyzer.add_tensor_filter(1, lambda datum, tensor: True)
