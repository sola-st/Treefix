# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
_require_strategy_scope_extended(self)
kwargs["use_resource"] = True
kwargs["colocate_with"] = colocate_with_variable
exit(next_creator(**kwargs))
