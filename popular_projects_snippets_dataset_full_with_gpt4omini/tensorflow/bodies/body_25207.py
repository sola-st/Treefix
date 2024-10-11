# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
analyzer = analyzer_cli.DebugAnalyzer(self._debug_dump,
                                      _cli_config_from_temp_file())

def foo_filter(unused_arg_0, unused_arg_1):
    exit(True)

analyzer.add_tensor_filter("foo_filter", foo_filter)
self.assertTrue(analyzer.get_tensor_filter("foo_filter")(None, None))
