# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Configures the model for training.

    Args:
        optimizer: String (name of optimizer) or optimizer instance. See
          `tf.keras.optimizers`.
        loss: String (name of objective function), objective function or
          `tf.keras.losses.Loss` instance. See `tf.keras.losses`. An objective
          function is any callable with the signature `loss = fn(y_true,
          y_pred)`, where y_true = ground truth values with shape =
          `[batch_size, d0, .. dN]`, except sparse loss functions such as sparse
          categorical crossentropy where shape = `[batch_size, d0, .. dN-1]`.
          y_pred = predicted values with shape = `[batch_size, d0, .. dN]`. It
          returns a weighted loss float tensor. If a custom `Loss` instance is
          used and reduction is set to `None`, return value has the shape
          `[batch_size, d0, .. dN-1]` i.e. per-sample or per-timestep loss
          values; otherwise, it is a scalar. If the model has multiple outputs,
          you can use a different loss on each output by passing a dictionary
          or a list of losses. The loss value that will be minimized by the
          model will then be the sum of all individual losses, unless
          `loss_weights` is specified.
        metrics: List of metrics to be evaluated by the model during training
          and testing. Each of this can be a string (name of a built-in
          function), function or a `tf.keras.metrics.Metric` instance. See
          `tf.keras.metrics`. Typically you will use `metrics=['accuracy']`. A
          function is any callable with the signature `result = fn(y_true,
          y_pred)`. To specify different metrics for different outputs of a
          multi-output model, you could also pass a dictionary, such as
          `metrics={'output_a': 'accuracy', 'output_b': ['accuracy', 'mse']}`.
          You can also pass a list to specify a metric or a list of metrics
          for each output, such as `metrics=[['accuracy'], ['accuracy', 'mse']]`
          or `metrics=['accuracy', ['accuracy', 'mse']]`. When you pass the
          strings 'accuracy' or 'acc', we convert this to one of
          `tf.keras.metrics.BinaryAccuracy`,
          `tf.keras.metrics.CategoricalAccuracy`,
          `tf.keras.metrics.SparseCategoricalAccuracy` based on the loss
          function used and the model output shape. We do a similar
          conversion for the strings 'crossentropy' and 'ce' as well.
        loss_weights: Optional list or dictionary specifying scalar coefficients
          (Python floats) to weight the loss contributions of different model
          outputs. The loss value that will be minimized by the model will then
          be the *weighted sum* of all individual losses, weighted by the
          `loss_weights` coefficients.
            If a list, it is expected to have a 1:1 mapping to the model's
              outputs. If a dict, it is expected to map output names (strings)
              to scalar coefficients.
        weighted_metrics: List of metrics to be evaluated and weighted by
          `sample_weight` or `class_weight` during training and testing.
        run_eagerly: Bool. Defaults to `False`. If `True`, this `Model`'s
          logic will not be wrapped in a `tf.function`. Recommended to leave
          this as `None` unless your `Model` cannot be run inside a
          `tf.function`. `run_eagerly=True` is not supported when using
          `tf.distribute.experimental.ParameterServerStrategy`.
        steps_per_execution: Int. Defaults to 1. The number of batches to
          run during each `tf.function` call. Running multiple batches
          inside a single `tf.function` call can greatly improve performance
          on TPUs or small models with a large Python overhead.
          At most, one full epoch will be run each
          execution. If a number larger than the size of the epoch is passed,
          the execution will be truncated to the size of the epoch.
          Note that if `steps_per_execution` is set to `N`,
          `Callback.on_batch_begin` and `Callback.on_batch_end` methods
          will only be called every `N` batches
          (i.e. before/after each `tf.function` execution).
        **kwargs: Arguments supported for backwards compatibility only.

    Raises:
        ValueError: In case of invalid arguments for
            `optimizer`, `loss` or `metrics`.
    """
with self.distribute_strategy.scope():
    if 'experimental_steps_per_execution' in kwargs:
        logging.warning('The argument `steps_per_execution` is no longer '
                        'experimental. Pass `steps_per_execution` instead of '
                        '`experimental_steps_per_execution`.')
        if not steps_per_execution:
            steps_per_execution = kwargs.pop('experimental_steps_per_execution')

      # When compiling from an already-serialized model, we do not want to
      # reapply some processing steps (e.g. metric renaming for multi-output
      # models, which have prefixes added for each corresponding output name).
    from_serialized = kwargs.pop('from_serialized', False)

    self._validate_compile(optimizer, metrics, **kwargs)
    self._run_eagerly = run_eagerly

    self.optimizer = self._get_optimizer(optimizer)
    self.compiled_loss = compile_utils.LossesContainer(
        loss, loss_weights, output_names=self.output_names)
    self.compiled_metrics = compile_utils.MetricsContainer(
        metrics, weighted_metrics, output_names=self.output_names,
        from_serialized=from_serialized)

    self._configure_steps_per_execution(steps_per_execution or 1)

    # Initializes attrs that are reset each time `compile` is called.
    self._reset_compile_cache()
    self._is_compiled = True

    self.loss = loss or {}  # Backwards compat.
