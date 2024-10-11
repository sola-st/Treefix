# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Returns the loss value & metrics values for the model in test mode.

    Computation is done in batches (see the `batch_size` arg.)

    Args:
        x: Input data. It could be:
          - A Numpy array (or array-like), or a list of arrays
            (in case the model has multiple inputs).
          - A TensorFlow tensor, or a list of tensors
            (in case the model has multiple inputs).
          - A dict mapping input names to the corresponding array/tensors,
            if the model has named inputs.
          - A `tf.data` dataset. Should return a tuple
            of either `(inputs, targets)` or
            `(inputs, targets, sample_weights)`.
          - A generator or `keras.utils.Sequence` returning `(inputs, targets)`
            or `(inputs, targets, sample_weights)`.
          A more detailed description of unpacking behavior for iterator types
          (Dataset, generator, Sequence) is given in the `Unpacking behavior
          for iterator-like inputs` section of `Model.fit`.
        y: Target data. Like the input data `x`, it could be either Numpy
          array(s) or TensorFlow tensor(s). It should be consistent with `x`
          (you cannot have Numpy inputs and tensor targets, or inversely). If
          `x` is a dataset, generator or `keras.utils.Sequence` instance, `y`
          should not be specified (since targets will be obtained from the
          iterator/dataset).
        batch_size: Integer or `None`. Number of samples per batch of
          computation. If unspecified, `batch_size` will default to 32. Do not
          specify the `batch_size` if your data is in the form of a dataset,
          generators, or `keras.utils.Sequence` instances (since they generate
          batches).
        verbose: 0 or 1. Verbosity mode. 0 = silent, 1 = progress bar.
        sample_weight: Optional Numpy array of weights for the test samples,
          used for weighting the loss function. You can either pass a flat (1D)
          Numpy array with the same length as the input samples
            (1:1 mapping between weights and samples), or in the case of
              temporal data, you can pass a 2D array with shape `(samples,
              sequence_length)`, to apply a different weight to every timestep
              of every sample. This argument is not supported when `x` is a
              dataset, instead pass sample weights as the third element of `x`.
        steps: Integer or `None`. Total number of steps (batches of samples)
          before declaring the evaluation round finished. Ignored with the
          default value of `None`. If x is a `tf.data` dataset and `steps` is
          None, 'evaluate' will run until the dataset is exhausted. This
          argument is not supported with array inputs.
        callbacks: List of `keras.callbacks.Callback` instances. List of
          callbacks to apply during evaluation. See
          [callbacks](/api_docs/python/tf/keras/callbacks).
        max_queue_size: Integer. Used for generator or `keras.utils.Sequence`
          input only. Maximum size for the generator queue. If unspecified,
          `max_queue_size` will default to 10.
        workers: Integer. Used for generator or `keras.utils.Sequence` input
          only. Maximum number of processes to spin up when using process-based
          threading. If unspecified, `workers` will default to 1.
        use_multiprocessing: Boolean. Used for generator or
          `keras.utils.Sequence` input only. If `True`, use process-based
          threading. If unspecified, `use_multiprocessing` will default to
          `False`. Note that because this implementation relies on
          multiprocessing, you should not pass non-picklable arguments to the
          generator as they can't be passed easily to children processes.
        return_dict: If `True`, loss and metric results are returned as a dict,
          with each key being the name of the metric. If `False`, they are
          returned as a list.
        **kwargs: Unused at this time.

    See the discussion of `Unpacking behavior for iterator-like inputs` for
    `Model.fit`.

    `Model.evaluate` is not yet supported with
    `tf.distribute.experimental.ParameterServerStrategy`.

    Returns:
        Scalar test loss (if the model has a single output and no metrics)
        or list of scalars (if the model has multiple outputs
        and/or metrics). The attribute `model.metrics_names` will give you
        the display labels for the scalar outputs.

    Raises:
        RuntimeError: If `model.evaluate` is wrapped in `tf.function`.
        ValueError: in case of invalid arguments.
    """
version_utils.disallow_legacy_graph('Model', 'evaluate')
self._assert_compile_was_called()
self._check_call_args('evaluate')
_disallow_inside_tf_function('evaluate')
use_cached_eval_dataset = kwargs.pop('_use_cached_eval_dataset', False)
if kwargs:
    raise TypeError('Invalid keyword arguments: %s' % (kwargs,))

if self.distribute_strategy._should_use_with_coordinator:  # pylint: disable=protected-access
    self._cluster_coordinator = cluster_coordinator.ClusterCoordinator(
        self.distribute_strategy)

with self.distribute_strategy.scope():
    # Use cached evaluation data only when it's called in `Model.fit`
    if (use_cached_eval_dataset
        and getattr(self, '_eval_data_handler', None) is not None):
        data_handler = self._eval_data_handler
    else:
        # Creates a `tf.data.Dataset` and handles batch and epoch iteration.
        data_handler = data_adapter.get_data_handler(
            x=x,
            y=y,
            sample_weight=sample_weight,
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

    logs = {}
    self.test_function = self.make_test_function()
    self._test_counter.assign(0)
    callbacks.on_test_begin()
    for _, iterator in data_handler.enumerate_epochs():  # Single epoch.
        self.reset_metrics()
        with data_handler.catch_stop_iteration():
            for step in data_handler.steps():
                with trace.Trace('test', step_num=step, _r=1):
                    callbacks.on_test_batch_begin(step)
                    tmp_logs = self.test_function(iterator)
                    if data_handler.should_sync:
                        context.async_wait()
                    logs = tmp_logs  # No error, now safe to assign to logs.
                    end_step = step + data_handler.step_increment
                    callbacks.on_test_batch_end(end_step, logs)
    logs = tf_utils.sync_to_numpy_or_python_type(logs)
    callbacks.on_test_end(logs=logs)

    if return_dict:
        exit(logs)
    else:
        exit(flatten_metrics_in_order(logs, self.metrics_names))
