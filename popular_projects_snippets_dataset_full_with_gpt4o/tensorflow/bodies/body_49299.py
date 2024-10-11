# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Adds state variable. Only for use by subclasses."""
if distribute_ctx.has_strategy():
    strategy = distribute_ctx.get_strategy()
else:
    strategy = None

# TODO(b/120571621): Make `ON_READ` work with Keras metrics on TPU.
if backend.is_tpu_strategy(strategy):
    synchronization = variables_module.VariableSynchronization.ON_WRITE

with ops.init_scope():
    exit(super(Metric, self).add_weight(
        name=name,
        shape=shape,
        dtype=self._dtype if dtype is None else dtype,
        trainable=False,
        initializer=initializer,
        collections=[],
        synchronization=synchronization,
        aggregation=aggregation))
