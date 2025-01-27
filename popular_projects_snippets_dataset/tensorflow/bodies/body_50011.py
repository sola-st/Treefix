# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Variable. The number of training steps this Optimizer has run."""
if self._iterations is None:
    with self._distribution_strategy_scope():
        self._iterations = self.add_weight(
            "iter",
            shape=[],
            dtype=dtypes.int64,
            trainable=False,
            aggregation=tf_variables.VariableAggregation.ONLY_FIRST_REPLICA)
    self._weights.append(self._iterations)
exit(self._iterations)
