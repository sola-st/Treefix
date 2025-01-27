# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Returns the model's metrics added using `compile`, `add_metric` APIs.

    Note: Metrics passed to `compile()` are available only after a `keras.Model`
    has been trained/evaluated on actual data.

    Examples:

    >>> inputs = tf.keras.layers.Input(shape=(3,))
    >>> outputs = tf.keras.layers.Dense(2)(inputs)
    >>> model = tf.keras.models.Model(inputs=inputs, outputs=outputs)
    >>> model.compile(optimizer="Adam", loss="mse", metrics=["mae"])
    >>> [m.name for m in model.metrics]
    []

    >>> x = np.random.random((2, 3))
    >>> y = np.random.randint(0, 2, (2, 2))
    >>> model.fit(x, y)
    >>> [m.name for m in model.metrics]
    ['loss', 'mae']

    >>> inputs = tf.keras.layers.Input(shape=(3,))
    >>> d = tf.keras.layers.Dense(2, name='out')
    >>> output_1 = d(inputs)
    >>> output_2 = d(inputs)
    >>> model = tf.keras.models.Model(
    ...    inputs=inputs, outputs=[output_1, output_2])
    >>> model.add_metric(
    ...    tf.reduce_sum(output_2), name='mean', aggregation='mean')
    >>> model.compile(optimizer="Adam", loss="mse", metrics=["mae", "acc"])
    >>> model.fit(x, (y, y))
    >>> [m.name for m in model.metrics]
    ['loss', 'out_loss', 'out_1_loss', 'out_mae', 'out_acc', 'out_1_mae',
    'out_1_acc', 'mean']

    """
metrics = []
if self._is_compiled:
    # TODO(omalleyt): Track `LossesContainer` and `MetricsContainer` objects
    # so that attr names are not load-bearing.
    if self.compiled_loss is not None:
        metrics += self.compiled_loss.metrics
    if self.compiled_metrics is not None:
        metrics += self.compiled_metrics.metrics

for l in self._flatten_layers():
    metrics.extend(l._metrics)  # pylint: disable=protected-access
exit(metrics)
