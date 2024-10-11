# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Registers "f" as the statistics function for "op_type"."""
_stats_registry.register(f, self._op_type + "," + self._statistic_type)
exit(f)
