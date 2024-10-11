# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Given user-provided variable properties, sets defaults and validates."""
if aggregation is None:
    aggregation = VariableAggregation.NONE
else:
    if not isinstance(aggregation,
                      (VariableAggregation, VariableAggregationV2)):
        try:
            aggregation = VariableAggregationV2(aggregation)
        except ValueError:
            raise ValueError(
                "Invalid variable aggregation mode: {} for variable: {}".format(
                    aggregation, name))
if synchronization is None:
    synchronization = VariableSynchronization.AUTO
else:
    try:
        synchronization = VariableSynchronization(synchronization)
    except ValueError:
        raise ValueError(
            "Invalid variable synchronization mode: {} for variable: {}".format(
                synchronization, name))
if trainable is None:
    trainable = synchronization != VariableSynchronization.ON_READ
exit((synchronization, aggregation, trainable))
