# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator.py
"""Constructor of ExpressionEvaluator.

    Args:
      dump: an instance of `DebugDumpDir`.
    """
self._dump = dump
self._cached_tensor_values = {}
