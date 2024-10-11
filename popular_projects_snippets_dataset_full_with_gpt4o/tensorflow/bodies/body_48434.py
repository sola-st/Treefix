# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
"""Fits the state of the preprocessing layer to the data being passed.

    After calling `adapt` on a layer, a preprocessing layer's state will not
    update during training. In order to make preprocessing layers efficient in
    any distribution context, they are kept constant with respect to any
    compiled `tf.Graph`s that call the layer. This does not affect the layer use
    when adapting each layer only once, but if you adapt a layer multiple times
    you will need to take care to re-compile any compiled functions as follows:

     * If you are adding a preprocessing layer to a `keras.Model`, you need to
       call `model.compile` after each subsequent call to `adapt`.
     * If you are calling a preprocessing layer inside `tf.data.Dataset.map`,
       you should call `map` again on the input `tf.data.Dataset` after each
       `adapt`.
     * If you are using a `tf.function` directly which calls a preprocessing
       layer, you need to call `tf.function` again on your callable after
       each subsequent call to `adapt`.

    `tf.keras.Model` example with multiple adapts:

    >>> layer = tf.keras.layers.experimental.preprocessing.Normalization(
    ...     axis=None)
    >>> layer.adapt([0, 2])
    >>> model = tf.keras.Sequential(layer)
    >>> model.predict([0, 1, 2])
    array([-1.,  0.,  1.], dtype=float32)
    >>> layer.adapt([-1, 1])
    >>> model.compile() # This is needed to re-compile model.predict!
    >>> model.predict([0, 1, 2])
    array([0., 1., 2.], dtype=float32)

    `tf.data.Dataset` example with multiple adapts:

    >>> layer = tf.keras.layers.experimental.preprocessing.Normalization(
    ...     axis=None)
    >>> layer.adapt([0, 2])
    >>> input_ds = tf.data.Dataset.range(3)
    >>> normalized_ds = input_ds.map(layer)
    >>> list(normalized_ds.as_numpy_iterator())
    [array([-1.], dtype=float32),
     array([0.], dtype=float32),
     array([1.], dtype=float32)]
    >>> layer.adapt([-1, 1])
    >>> normalized_ds = input_ds.map(layer) # Re-map over the input dataset.
    >>> list(normalized_ds.as_numpy_iterator())
    [array([0.], dtype=float32),
     array([1.], dtype=float32),
     array([2.], dtype=float32)]

    Arguments:
        data: The data to train on. It can be passed either as a tf.data
          Dataset, or as a numpy array.
        batch_size: Integer or `None`.
            Number of samples per state update.
            If unspecified, `batch_size` will default to 32.
            Do not specify the `batch_size` if your data is in the
            form of datasets, generators, or `keras.utils.Sequence` instances
            (since they generate batches).
        steps: Integer or `None`.
            Total number of steps (batches of samples)
            When training with input tensors such as
            TensorFlow data tensors, the default `None` is equal to
            the number of samples in your dataset divided by
            the batch size, or 1 if that cannot be determined. If x is a
            `tf.data` dataset, and 'steps' is None, the epoch will run until
            the input dataset is exhausted. When passing an infinitely
            repeating dataset, you must specify the `steps` argument. This
            argument is not supported with array inputs.
        reset_state: Optional argument specifying whether to clear the state of
          the layer at the start of the call to `adapt`, or whether to start
          from the existing state. This argument may not be relevant to all
          preprocessing layers: a subclass of PreprocessingLayer may choose to
          throw if 'reset_state' is set to False.
    """
_disallow_inside_tf_function('adapt')
if not version_utils.should_use_v2():
    raise RuntimeError('`adapt` is only supported in tensorflow v2.')  # pylint: disable=g-doc-exception
if not self.streaming and self._is_adapted and not reset_state:
    raise ValueError('{} does not supporting calling `adapt` twice without '
                     'resetting the state.'.format(self.__class__.__name__))
if not self._is_compiled:
    self.compile()  # Compile with defaults.
if self.built and reset_state:
    self.reset_state()
data_handler = data_adapter.DataHandler(
    data,
    batch_size=batch_size,
    steps_per_epoch=steps,
    epochs=1,
    steps_per_execution=self._steps_per_execution,
    distribute=False)
self._adapt_function = self.make_adapt_function()
for _, iterator in data_handler.enumerate_epochs():
    with data_handler.catch_stop_iteration():
        for _ in data_handler.steps():
            self._adapt_function(iterator)
            if data_handler.should_sync:
                context.async_wait()
self.finalize_state()
self._is_adapted = True
