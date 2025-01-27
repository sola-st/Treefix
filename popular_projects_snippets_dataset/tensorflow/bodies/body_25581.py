# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""DebugAnalyzer constructor.

    Args:
      debug_dump: A DebugDumpDir object.
      config: A `cli_config.CLIConfig` object that carries user-facing
        configurations.
    """

self._debug_dump = debug_dump
self._evaluator = evaluator.ExpressionEvaluator(self._debug_dump)

# Initialize tensor filters state.
self._tensor_filters = {}

self._build_argument_parsers(config)
config.set_callback("graph_recursion_depth",
                    self._build_argument_parsers)
