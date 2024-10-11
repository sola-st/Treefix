# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
if self._hypers_created:
    exit()
with self._distribution_strategy_scope():
    # Iterate hyper values deterministically.
    for name, value in sorted(self._hyper.items()):
        if isinstance(value,
                      (ops.Tensor, tf_variables.Variable)) or callable(value):
            # The check for `callable` covers the usage when `value` is a
            # `LearningRateSchedule`, in which case it does not need to create a
            # variable.
            continue
        else:
            self._hyper[name] = self.add_weight(
                name,
                shape=[],
                trainable=False,
                initializer=value,
                aggregation=tf_variables.VariableAggregation.ONLY_FIRST_REPLICA)
self._hypers_created = True
