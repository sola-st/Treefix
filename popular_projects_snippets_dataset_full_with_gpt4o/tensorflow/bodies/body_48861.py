# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_arrays_v1.py
"""Loop function for arrays of data with modes TRAIN/TEST/PREDICT.

  Args:
      model: Keras Model instance.
      inputs: Either a list or dictionary of arrays, or a dataset instance.
      targets: List/dictionary of input arrays.
      sample_weights: Optional list of sample weight arrays.
      batch_size: Integer batch size or None if unknown.
      epochs: Number of times to iterate over the data
      verbose: 0, 1, or 2. Verbosity mode.
        0 = silent, 1 = progress bar, 2 = one line per epoch.
        Note that the progress bar is not particularly useful when
        logged to a file, so verbose=2 is recommended when not running
        interactively (eg, in a production environment).
      callbacks: List of callbacks to be called during training
      val_inputs: Either a list or dictionary of arrays, or a dataset instance.
      val_targets: List/dictionary of target arrays.
      val_sample_weights: Optional list of sample weight arrays.
      shuffle: Whether to shuffle the data at the beginning of each epoch
        concatenation of list the display names of the outputs of `f` and the
        list of display names of the outputs of `f_val`.
      initial_epoch: Epoch at which to start training (useful for resuming a
        previous training run)
      steps_per_epoch: Total number of steps (batches of samples) before
        declaring one epoch finished and starting the next epoch. Ignored with
        the default value of `None`.
      validation_steps: Number of steps to run validation for (only if doing
        validation from data tensors). Ignored with the default value of
        `None`.
      validation_freq: Only relevant if validation data is provided. Integer or
        `collections.abc.Container` instance (e.g. list, tuple, etc.). If an
        integer, specifies how many training epochs to run before a new
        validation run is performed, e.g. `validation_freq=2` runs
        validation every 2 epochs. If a Container, specifies the epochs on
        which to run validation, e.g. `validation_freq=[1, 2, 10]` runs
        validation at the end of the 1st, 2nd, and 10th epochs.
      mode: One of ModeKeys.TRAIN/ModeKeys.TEST/ModeKeys.PREDICT.
      validation_in_fit: if true, then this method is invoked from within
        training iteration (for validation). In the case where `val_inputs` is
        a dataset, this flag indicates that its iterator and feed values are
        already created so should properly reuse resources.
      prepared_feed_values_from_dataset: if True, `inputs` is a list of feed
        tensors returned from `_prepare_feed_values` call on the validation
        dataset, so do not call it again on `inputs`. Should only be used for
        inline validation (i.e., only if `validation_in_fit` is also True).
      steps_name: The string name of the steps argument, either `steps`,
        `validation_steps`, or `steps_per_epoch`. Only used for error message
        formatting.
      **kwargs: Additional arguments for backwards compatibility.

  Returns:
      - In TRAIN mode: `History` object.
      - In TEST mode: Evaluation metrics.
      - In PREDICT mode: Outputs of the Model called on inputs.

  Raises:
      ValueError: in case of invalid arguments.
  """
# Backwards compatibility.
if 'steps' in kwargs:
    steps_per_epoch = kwargs.pop('steps')
if kwargs:
    raise TypeError('Unknown arguments: %s' % (kwargs,))

# In case we were passed a dataset, we extract symbolic tensors from it.
reset_dataset_after_each_epoch = False
input_iterator = None
is_dataset = isinstance(inputs,
                        (dataset_ops.DatasetV1, dataset_ops.DatasetV2))
# TODO(fchollet): consider moving `steps_per_epoch` inference to
# _standardize_user_data and set reset_dataset_after_each_epoch as an
# attribute on the dataset instance.
if is_dataset:
    if steps_per_epoch is None:
        reset_dataset_after_each_epoch = True
        steps_per_epoch = training_utils_v1.infer_steps_for_dataset(
            model, inputs, steps_per_epoch, epochs=epochs, steps_name=steps_name)
    input_iterator = _get_iterator(inputs, model._distribution_strategy)

# Enter tf.distribute.Strategy scope.
if model._distribution_strategy:
    scope = distributed_training_utils_v1.distributed_scope(
        strategy=model._distribution_strategy,
        learning_phase=(1 if mode == ModeKeys.TRAIN else 0))
    scope.__enter__()

use_steps = is_dataset or steps_per_epoch is not None
do_validation = val_inputs is not None

# Prepare input data.
inputs = input_iterator or inputs
if validation_in_fit and prepared_feed_values_from_dataset:
    # When invoking validation in training loop, avoid creating iterator and
    # list of feed values for the same validation dataset multiple times (which
    # essentially would call `iterator.get_next()` that slows down execution and
    # leads to OOM errors eventually.
    ins = inputs
else:
    ins = _prepare_feed_values(model, inputs, targets, sample_weights, mode)
    # `ins` is a function when a distribute strategy is used in Eager mode.  In
    # that case `is_dataset` is True.  The code branches that have requirements
    # about the type of `ins` do not trigger in the distributed case.

if not is_dataset:
    num_samples_or_steps = _get_num_samples_or_steps(ins, batch_size,
                                                     steps_per_epoch)
else:
    num_samples_or_steps = steps_per_epoch

# Update sample_weight_mode of the model if sample_weights is specified by the
# user. We need to call this function after we have a handle on the inputs
# (both numpy arrays and datasets) in order to determine if the user has
# specified sample_weights.
_update_sample_weight_mode(model, mode, ins)

# Get step function and loop type. As part of building the execution
# function we recompile the metrics based on the updated
# sample_weight_mode value.
f = _make_execution_function(model, mode)

# Prepare validation data. Hold references to the iterator and the input list
# to properly reinitialize and reuse in multiple validation passes.
val_iterator = None
if isinstance(val_inputs, (dataset_ops.DatasetV1, dataset_ops.DatasetV2)):
    if validation_steps is None:
        # Because we pass an iterator feed instead of a Dataset to the eval
        # model_iteration() call, it will not trigger the dataset-input path
        # that determines the number of steps required. To avoid this issue,
        # set validation_steps here if validation_steps is None.
        validation_steps = training_utils_v1.infer_steps_for_dataset(
            model,
            val_inputs,
            validation_steps,
            epochs=epochs,
            steps_name='validation_steps')
    val_iterator = _get_iterator(val_inputs, model._distribution_strategy)
    val_inputs = _prepare_feed_values(
        model, val_iterator, val_targets, val_sample_weights, ModeKeys.TEST)
    # Get num steps for printing.
    val_samples_or_steps = validation_steps
else:
    # Get num samples for printing.
    val_samples_or_steps = val_inputs and nest.flatten(
        val_inputs)[0].shape[0] or None

if mode == ModeKeys.TRAIN and verbose:
    _print_train_info(num_samples_or_steps, val_samples_or_steps, is_dataset)

# Configure callbacks.
count_mode = 'steps' if use_steps else 'samples'
callbacks = cbks.configure_callbacks(
    callbacks,
    model,
    do_validation=do_validation,
    batch_size=batch_size,
    epochs=epochs,
    steps_per_epoch=steps_per_epoch,
    samples=num_samples_or_steps,
    count_mode=count_mode,
    verbose=verbose,
    mode=mode)

# Find beforehand arrays that need sparse-to-dense conversion.
if issparse is not None and not use_steps:
    indices_for_conversion_to_dense = []
    feed = _get_model_feed(model, mode)
    for i, (input_data, feed_tensor) in enumerate(zip(ins, feed)):
        if issparse(input_data) and not backend.is_sparse(feed_tensor):
            indices_for_conversion_to_dense.append(i)

  # Select aggregation method.
if mode == ModeKeys.PREDICT:
    aggregator = training_utils_v1.OutputsAggregator(
        use_steps,
        num_samples=None if steps_per_epoch else num_samples_or_steps,
        steps=steps_per_epoch)
else:
    aggregator = training_utils_v1.MetricsAggregator(
        use_steps,
        num_samples=None if steps_per_epoch else num_samples_or_steps,
        steps=steps_per_epoch)

if model._compile_distribution:
    distributed_training_utils_v1._copy_weights_to_distributed_model(
        model, mode)

callbacks.model.stop_training = False
callbacks._call_begin_hook(mode)

initial_epoch = model._maybe_load_initial_epoch_from_ckpt(initial_epoch, mode)

for epoch in range(initial_epoch, epochs):
    if callbacks.model.stop_training:
        break

    # Setup work for each epoch
    epoch_logs = {}
    if mode != ModeKeys.PREDICT:
        # Collecting and resetting metrics has non-zero cost and will needlessly
        # slow down model.predict.
        model.reset_metrics()
    if mode == ModeKeys.TRAIN:
        callbacks.on_epoch_begin(epoch, epoch_logs)

    if use_steps:
        # Step-wise loop.
        if steps_per_epoch is None:
            # Loop over dataset until `OutOfRangeError` is raised.
            target_steps = np.inf
        else:
            # Loop over dataset for the specified number of steps.
            target_steps = steps_per_epoch

        step = 0
        while step < target_steps:
            batch_logs = {'batch': step, 'size': 1}
            callbacks._call_batch_hook(mode, 'begin', step, batch_logs)

            # Get outputs.
            try:
                # `ins` can be callable in tf.distribute.Strategy + eager case.
                if not callable(ins) or (model._distribution_strategy and
                                         not distributed_training_utils_v1
                                         .is_distributing_by_cloning(model)):
                    actual_inputs = ins
                else:
                    actual_inputs = ins()
                batch_outs = f(actual_inputs)
            except errors.OutOfRangeError:
                if is_dataset:
                    # The dataset passed by the user ran out of batches.
                    # Now we know the cardinality of the dataset.
                    # If steps_per_epoch was specified, then running out of data is
                    # unexpected, so we stop training and inform the user.
                    if steps_per_epoch:
                        callbacks.model.stop_training = True
                        logging.warning(
                            'Your dataset ran out of data; interrupting training. '
                            'Make sure that your dataset can generate at least '
                            '`%s * epochs` batches (in this case, %d batches). '
                            'You may need to use the repeat() function when '
                            'building your dataset.'
                            % (steps_name, steps_per_epoch * epochs))
                    elif step > 0:
                        steps_per_epoch = step
                        aggregator.steps = steps_per_epoch
                else:
                    # We ran out of batches while the user passed an iterator (legacy).
                    callbacks.model.stop_training = True
                    logging.warning(
                        'Your dataset iterator ran out of data; '
                        'interrupting training. Make sure that your iterator '
                        'can generate at least `%s * epochs` '
                        'batches (in this case, %d batches). You may need to'
                        'use the repeat() function when building your '
                        'dataset.' % (steps_name, steps_per_epoch * epochs))
                break

            if not isinstance(batch_outs, list):
                batch_outs = [batch_outs]

            if model._distribution_strategy:
                batch_outs = (
                    distributed_training_utils_v1._per_replica_aggregate_batch(
                        model._distribution_strategy, batch_outs, model, mode))

            # Aggregate results.
            if step == 0:
                aggregator.create(batch_outs)
            aggregator.aggregate(batch_outs)

            # Callbacks batch end.
            batch_logs = cbks.make_logs(model, batch_logs, batch_outs, mode)
            callbacks._call_batch_hook(mode, 'end', step, batch_logs)
            step += 1

            if callbacks.model.stop_training:
                break
    else:
        # Sample-wise loop.
        index_array = np.arange(num_samples_or_steps)
        if shuffle == 'batch':
            index_array = training_utils_v1.batch_shuffle(index_array, batch_size)
        elif shuffle:
            np.random.shuffle(index_array)
        batches = make_batches(num_samples_or_steps, batch_size)
        for batch_index, (batch_start, batch_end) in enumerate(batches):
            batch_ids = index_array[batch_start:batch_end]
            # Slice into a batch.
            if len(batches) == 1:
                # If we only have one batch, do not slice. This takes care of
                # composite tensors in non-Dataset modes; we currently don't support
                # slicing them.
                # TODO(b/133517906): Add slicing support.
                ins_batch = ins
            else:
                try:
                    if ins and isinstance(ins[-1], int):
                        # Do not slice the training phase flag.
                        ins_batch = slice_arrays(ins[:-1], batch_ids) + [ins[-1]]
                    else:
                        ins_batch = slice_arrays(ins, batch_ids)
                except TypeError:
                    raise TypeError('TypeError while preparing batch. '
                                    'If using HDF5 input data, '
                                    'pass shuffle="batch".')

        # Sparse to dense conversion.
            if issparse is not None:
                for i in indices_for_conversion_to_dense:
                    ins_batch[i] = ins_batch[i].toarray()

        # Callbacks batch_begin.
            batch_logs = {'batch': batch_index, 'size': len(batch_ids)}
            callbacks._call_batch_hook(mode, 'begin', batch_index, batch_logs)

            # Get outputs.
            batch_outs = f(ins_batch)
            if not isinstance(batch_outs, list):
                batch_outs = [batch_outs]

            # Aggregate results.
            if batch_index == 0:
                aggregator.create(batch_outs)
            aggregator.aggregate(batch_outs, batch_start, batch_end)

            # Callbacks batch end.
            batch_logs = cbks.make_logs(model, batch_logs, batch_outs, mode)
            callbacks._call_batch_hook(mode, 'end', batch_index, batch_logs)

            if callbacks.model.stop_training:
                break

    aggregator.finalize()
    results = aggregator.results
    epoch_logs = cbks.make_logs(model, epoch_logs, results, mode)
    if len(results) == 1:
        results = results[0]

    # Run the test loop every `validation_freq` epochs during training.
    if (do_validation and
        training_utils_v1.should_run_validation(validation_freq, epoch) and
        not callbacks.model.stop_training):

        if model._compile_distribution:
            # Since we create a new clone from the original model we need to copy
            # the weights back to the original model before we can run validation.
            distributed_training_utils_v1._copy_weights_to_original_model(
                model, ModeKeys.TRAIN)

        val_results = model_iteration(
            model,
            val_inputs,
            targets=val_targets,
            sample_weights=val_sample_weights,
            batch_size=batch_size,
            steps_per_epoch=validation_steps,
            callbacks=callbacks,
            verbose=0,
            mode=ModeKeys.TEST,
            validation_in_fit=True,
            prepared_feed_values_from_dataset=(val_iterator is not None),
            steps_name='validation_steps')
        if not isinstance(val_results, list):
            val_results = [val_results]
        epoch_logs = cbks.make_logs(
            model, epoch_logs, val_results, mode, prefix='val_')
        if val_iterator and epoch < epochs - 1:
            _reinitialize_iterator(val_iterator, model._distribution_strategy)

    if mode == ModeKeys.TRAIN:
        # Epochs only apply to `fit`.
        callbacks.on_epoch_end(epoch, epoch_logs)

    # Reinitialize dataset iterator for the next epoch.
    if reset_dataset_after_each_epoch and epoch < epochs - 1:
        _reinitialize_iterator(input_iterator, model._distribution_strategy)

model._successful_loop_finish = True
callbacks._call_end_hook(mode)

if model._distribution_strategy:
    if model._compile_distribution:
        # TODO(priyag, psv): Copy back metrics to the original model as well?
        distributed_training_utils_v1._copy_weights_to_original_model(model, mode)
    scope.__exit__(None, None, None)

if mode == ModeKeys.TRAIN:
    exit(model.history)
exit(results)
