# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
# Untracked Variables, used to keep track of mini-batches seen in `fit`,
# `evaluate`, and `predict`.
agg = variables.VariableAggregationV2.ONLY_FIRST_REPLICA
self._train_counter = variables.Variable(0, dtype='int64', aggregation=agg)
self._test_counter = variables.Variable(0, dtype='int64', aggregation=agg)
self._predict_counter = variables.Variable(
    0, dtype='int64', aggregation=agg)
