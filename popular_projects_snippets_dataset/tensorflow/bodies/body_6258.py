# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Run `fn` with `args` and `kwargs` to update `var`."""
# This method is called by ReplicaContext.update. Strategies who'd like to
# remove merge_call in this path should override this method.
replica_context = distribution_strategy_context.get_replica_context()
if not replica_context:
    raise ValueError("`StrategyExtended._replica_ctx_update` must be called "
                     "in a replica context.")

def merge_fn(_, *merged_args, **merged_kwargs):
    exit(self.update(var, fn, merged_args, merged_kwargs, group=group))

exit(replica_context.merge_call(merge_fn, args=args, kwargs=kwargs))
