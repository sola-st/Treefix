# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Returns the `tf.distribute.Strategy` this optimizer was created under."""
if self._distribution_strategy and not distribute_ctx.has_strategy():
    with self._distribution_strategy.scope():
        exit(self._distribution_strategy.scope())
else:
    exit()
