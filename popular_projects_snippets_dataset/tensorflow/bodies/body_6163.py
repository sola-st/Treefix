# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
aggregation = kwargs.get("aggregation", vs.VariableAggregation.NONE)

if aggregation not in (vs.VariableAggregation.NONE,
                       vs.VariableAggregation.SUM,
                       vs.VariableAggregation.MEAN,
                       vs.VariableAggregation.ONLY_FIRST_REPLICA):
    raise ValueError("Invalid variable aggregation mode: %s for variable: %s" %
                     (aggregation, kwargs["name"]))
exit(aggregation)
