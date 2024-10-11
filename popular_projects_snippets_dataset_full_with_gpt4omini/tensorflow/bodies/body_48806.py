# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Generates output predictions for the input samples.

    Computation is done in batches. This method is designed for performance in
    large scale inputs. For small amount of inputs that fit in one batch,
    directly using `__call__` is recommended for faster execution, e.g.,
    `model(x)`, or `model(x, training=False)` if you have layers such as
    `tf.keras.layers.BatchNormalization` that behaves differently during
    inference. Also, note the fact that test loss is not affected by
    regularization layers like noise and dropout.

    Args:
        x: Input samples. It could be:
          - A Numpy array (or array-like), or a list of arrays
            (in case the model has multiple inputs).
          - A TensorFlow tensor, or a list of tensors
            (in case the model has multiple inputs).
          - A `tf.data` dataset.
          - A generator or `keras.utils.Sequence` instance.
          A more detailed description of unpacking behavior for iterator types
          (Dataset, generator, Sequence) is given in the `Unpacking behavior
          for iterator-like inputs` section of `Model.fit`.
        batch_size: Integer or `None`.
            Number of samples per batch.
            If unspecified, `batch_size` will default to 32.
            Do not specify the `batch_size` if your data is in the
            form of dataset, generators, or `keras.utils.Sequence` instances
            (since they generate batches).
        verbose: Verbosity mode, 0 or 1.
        steps: Total number of steps (batches of samples)
            before declaring the prediction round finished.
            Ignored with the default value of `None`. If x is a `tf.data`
            dataset and `steps` is None, `predict` will
            run until the input dataset is exhausted.
        callbacks: List of `keras.callbacks.Callback` instances.
            List of callbacks to apply during prediction.
            See [callbacks](/api_docs/python/tf/keras/callbacks).
        max_queue_size: Integer. Used for generator or `keras.utils.Sequence`
            input only. Maximum size for the generator queue.
            If unspecified, `max_queue_size` will default to 10.
        workers: Integer. Used for generator or `keras.utils.Sequence` input
            only. Maximum number of processes to spin up when using
            process-based threading. If unspecified, `workers` will default
            to 1.
        use_multiprocessing: Boolean. Used for generator or
            `keras.utils.Sequence` input only. If `True`, use process-based
            threading. If unspecified, `use_multiprocessing` will default to
            `False`. Note that because this implementation relies on
            multiprocessing, you should not pass non-picklable arguments to
            the generator as they can't be passed easily to children processes.

    See the discussion of `Unpacking behavior for iterator-like inputs` for
    `Model.fit`. Note that Model.predict uses the same interpretation rules as
    `Model.fit` and `Model.evaluate`, so inputs must be unambiguous for all
    three methods.

    Returns:
        Numpy array(s) of predictions.

    Raises:
        RuntimeError: If `model.predict` is wrapped in `tf.function`.
        ValueError: In case of mismatch between the provided
            input data and the model's expectations,
            or in case a stateful model receives a number of samples
            that is not a multiple of the batch size.
    """
version_utils.disallow_legacy_graph('Model', 'predict')
self._check_call_args('predict')
_disallow_inside_tf_function('predict')

# TODO(yashkatariya): Cache model on the coordinator for faster prediction.
# If running under PSS, then swap it with OneDeviceStrategy so that
# execution will run on the coordinator.
original_pss_strategy = None
if self.distribute_strategy._should_use_with_coordinator:  # pylint: disable=protected-access
    original_pss_strategy = self.distribute_strategy
    self._distribution_strategy = None

# Cluster coordinator is set by `.fit()` and `.evaluate()` which is not
# needed in `.predict()` because all the predictions happen on the
# coordinator/locally.
if self._cluster_coordinator:
    self._cluster_coordinator = None

outputs = None
with self.distribute_strategy.scope():
    # Creates a `tf.data.Dataset` and handles batch and epoch iteration.
    dataset_types = (dataset_ops.DatasetV1, dataset_ops.DatasetV2)
    if (self._in_multi_worker_mode() or _is_tpu_multi_host(
        self.distribute_strategy)) and isinstance(x, dataset_types):
        try:
            options = options_lib.Options()
            data_option = options_lib.AutoShardPolicy.DATA
            options.experimental_distribute.auto_shard_policy = data_option
            x = x.with_options(options)
        except ValueError:
            warnings.warn('Using Model.predict with '
                          'MultiWorkerDistributionStrategy or TPUStrategy and '
                          'AutoShardPolicy.FILE might lead to out-of-order result'
                          '. Consider setting it to AutoShardPolicy.DATA.')

    data_handler = data_adapter.get_data_handler(
        x=x,
        batch_size=batch_size,
        steps_per_epoch=steps,
        initial_epoch=0,
        epochs=1,
        max_queue_size=max_queue_size,
        workers=workers,
        use_multiprocessing=use_multiprocessing,
        model=self,
        steps_per_execution=self._steps_per_execution)

    # Container that configures and calls `tf.keras.Callback`s.
    if not isinstance(callbacks, callbacks_module.CallbackList):
        callbacks = callbacks_module.CallbackList(
            callbacks,
            add_history=True,
            add_progbar=verbose != 0,
            model=self,
            verbose=verbose,
            epochs=1,
            steps=data_handler.inferred_steps)

    self.predict_function = self.make_predict_function()
    self._predict_counter.assign(0)
    callbacks.on_predict_begin()
    batch_outputs = None
    for _, iterator in data_handler.enumerate_epochs():  # Single epoch.
        with data_handler.catch_stop_iteration():
            for step in data_handler.steps():
                callbacks.on_predict_batch_begin(step)
                tmp_batch_outputs = self.predict_function(iterator)
                if data_handler.should_sync:
                    context.async_wait()
                batch_outputs = tmp_batch_outputs  # No error, now safe to assign.
                if outputs is None:
                    outputs = nest.map_structure(lambda batch_output: [batch_output],
                                                 batch_outputs)
                else:
                    nest.map_structure_up_to(
                        batch_outputs,
                        lambda output, batch_output: output.append(batch_output),
                        outputs, batch_outputs)
                end_step = step + data_handler.step_increment
                callbacks.on_predict_batch_end(end_step, {'outputs': batch_outputs})
    if batch_outputs is None:
        raise ValueError('Expect x to be a non-empty array or dataset.')
    callbacks.on_predict_end()
all_outputs = nest.map_structure_up_to(batch_outputs, concat, outputs)

# If originally PSS strategy was used, then replace it back since predict
# is running under `OneDeviceStrategy` after the swap and once its done
# we need to replace it back to PSS again.
if original_pss_strategy is not None:
    self._distribution_strategy = original_pss_strategy

exit(tf_utils.sync_to_numpy_or_python_type(all_outputs))
