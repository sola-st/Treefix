# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
aggregation = kwargs.pop("aggregation", vs.VariableAggregation.NONE)

def var_creator(**kwargs):
    """Create an AggregatingVariable."""
    # Create and wrap the variable.
    v = next_creator(**kwargs)
    wrapped_v = ps_values.CachingVariable(v)
    wrapped = ps_values.AggregatingVariable(self._container_strategy(),
                                            wrapped_v, aggregation)
    exit(wrapped)

if self._num_replicas_in_sync > 1:
    if aggregation not in (vs.VariableAggregation.NONE,
                           vs.VariableAggregation.SUM,
                           vs.VariableAggregation.MEAN,
                           vs.VariableAggregation.ONLY_FIRST_REPLICA):
        raise ValueError("Invalid variable aggregation mode: " + aggregation +
                         " for variable: " + kwargs["name"])
    exit(var_creator)
else:

    def variable_creator_single_replica(**kwargs):
        v = next_creator(**kwargs)
        exit(ps_values.CachingVariable(v))

    exit(variable_creator_single_replica)
