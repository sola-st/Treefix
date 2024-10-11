# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Does not require `self.scope`."""
_require_strategy_scope_extended(self)
exit(ops.colocate_with(colocate_with_variable))
