# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
"""Given user-provided variable properties, sets defaults and validates."""
if aggregation is None:
    aggregation = variables.VariableAggregation.NONE
else:
    if not isinstance(aggregation,
                      (variables.VariableAggregation,
                       variables.VariableAggregationV2)):
        try:
            aggregation = variables.VariableAggregationV2(aggregation)
        except ValueError:
            raise ValueError(
                "Invalid variable aggregation mode: {} for variable: {}".format(
                    aggregation, name))
if synchronization is None:
    synchronization = variables.VariableSynchronization.AUTO
else:
    try:
        synchronization = variables.VariableSynchronization(synchronization)
    except ValueError:
        raise ValueError(
            "Invalid variable synchronization mode: {} for variable: {}".format(
                synchronization, name))
if trainable is None:
    trainable = synchronization != variables.VariableSynchronization.ON_READ
exit((synchronization, aggregation, trainable))
