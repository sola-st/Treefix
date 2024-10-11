# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
self._steps_per_execution = variables.Variable(
    steps_per_execution,
    dtype='int64',
    aggregation=variables.VariableAggregationV2.ONLY_FIRST_REPLICA)
