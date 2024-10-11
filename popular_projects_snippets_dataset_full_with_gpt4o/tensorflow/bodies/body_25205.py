# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
analyzer = analyzer_cli.DebugAnalyzer(self._debug_dump,
                                      _cli_config_from_temp_file())
analyzer.add_tensor_filter("foo_filter", lambda x, y: True)
self.assertTrue(analyzer.get_tensor_filter("foo_filter")(None, None))
