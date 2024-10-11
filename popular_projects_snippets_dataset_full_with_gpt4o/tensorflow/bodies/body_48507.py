# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_generator_v1.py
"""Loop function for arrays of data with modes TRAIN/TEST/PREDICT.

  Args:
      model: Keras Model instance.
      data: Either a tuple of NumPy/Tensor inputs (i.e. `(x,)` or `(x, y)` or
        `(x, y, sample_weights)`) or a generator or
        `keras.utils.data_utils.Sequence` object or Eager Iterator or Dataset.
      steps_per_epoch: Total number of steps (batches of samples) before
        declaring one epoch finished and starting the next epoch. Ignored with
        the default value of `None`.
      epochs: Number of times to iterate over the data.
      verbose: 0, 1, or 2. Verbosity mode.
        0 = silent, 1 = progress bar, 2 = one line per epoch.
        Note that the progress bar is not particularly useful when
        logged to a file, so verbose=2 is recommended when not running
        interactively (eg, in a production environment).
      callbacks: List of callbacks to be called during training.
      validation_data: Either a tuple of NumPy/Tensor inputs (i.e. `(x,)` or
        `(x, y)` or `(x, y, sample_weights)`) or a generator or
        `keras.utils.data_utils.Sequence` object or Eager Iterator or Dataset.
      validation_steps: Total number of steps (batches of samples) before
        declaring validation finished.
      validation_freq: Only relevant if validation data is provided. Integer or
        `collections.abc.Container` instance (e.g. list, tuple, etc.). If an
        integer, specifies how many training epochs to run before a new
        validation run is performed, e.g. `validation_freq=2` runs
        validation every 2 epochs. If a Container, specifies the epochs on
        which to run validation, e.g. `validation_freq=[1, 2, 10]` runs
        validation at the end of the 1st, 2nd, and 10th epochs.
      class_weight: Dictionary mapping class indices to a weight for the class.
      max_queue_size: Integer. Maximum size for the generator queue. If
        unspecified, `max_queue_size` will default to 10.
      workers: Integer. Maximum number of processes to spin up when using
        process-based threading. If unspecified, `workers` will default to 1. If
        0, will execute the generator on the main thread.
      use_multiprocessing: Boolean. If `True`, use process-based threading. If
        unspecified, `use_multiprocessing` will default to `False`. Note that
        because this implementation relies on multiprocessing, you should not
        pass non-picklable arguments to the generator as they can't be passed
        easily to children processes.
      shuffle: Boolean. Whether to shuffle the order of the batches at the
        beginning of each epoch. Only used with instances of `Sequence`
        (`keras.utils.Sequence`). Has no effect when `steps_per_epoch` is not
        `None`.
      initial_epoch: Epoch at which to start training (useful for resuming a
        previous training run).
      mode: One of ModeKeys.TRAIN/ModeKeys.TEST/ModeKeys.PREDICT.
      batch_size: Integer batch size or None if unknown. Will only be used if
        `data` is in NumPy/Tensor format.
      steps_name: The string name of the steps argument, either `steps`,
        `validation_steps`, or `steps_per_epoch`. Only used for error message
        formatting.
      **kwargs: Additional arguments for backwards compatibility. `steps` is
        accepted as an alias for `steps_per_epoch`.

  Returns:
      - In TRAIN mode: `History` object.
      - In TEST mode: Evaluation metrics.
      - In PREDICT mode: Outputs of the Model called on inputs.

  Raises:
      ValueError: in case of invalid arguments.
  """
if 'steps' in kwargs:
    steps_per_epoch = kwargs['steps']

# Determine the number of steps per epoch and whether we should reset the
# dataset at the end of each epoch.
reset_dataset_after_each_epoch = False
original_dataset = None
is_dataset = isinstance(data, (dataset_ops.DatasetV2, dataset_ops.DatasetV1))
if is_dataset:
    original_dataset = data
    if steps_per_epoch is None:
        reset_dataset_after_each_epoch = True
        steps_per_epoch = training_utils_v1.infer_steps_for_dataset(
            model, data, steps_per_epoch, epochs=epochs, steps_name=steps_name)

  # Convert to a format that supports `next(generator)`.
generator, steps_per_epoch = convert_to_generator_like(
    data,
    steps_per_epoch=steps_per_epoch,
    batch_size=batch_size,
    epochs=epochs - initial_epoch,
    shuffle=shuffle)

do_validation = validation_data is not None
is_sequence = isinstance(generator, data_utils.Sequence)
_validate_arguments(is_sequence, is_dataset, use_multiprocessing, workers,
                    steps_per_epoch, validation_data, validation_steps, mode,
                    kwargs)

batch_function = _make_execution_function(
    model, mode, class_weight=class_weight)

# Create the queue for the generator.
enqueuer = None
if not is_dataset:
    generator, enqueuer = _make_enqueued_generator(
        generator,
        workers=workers,
        use_multiprocessing=use_multiprocessing,
        max_queue_size=max_queue_size,
        shuffle=shuffle)

num_samples_or_steps, use_steps = _get_num_samples_or_steps(
    data, steps_per_epoch)

count_mode = 'steps' if use_steps else 'samples'
callbacks = cbks.configure_callbacks(
    callbacks,
    model,
    do_validation=do_validation,
    epochs=epochs,
    steps_per_epoch=steps_per_epoch,
    batch_size=batch_size,
    samples=num_samples_or_steps,
    count_mode=count_mode,
    verbose=verbose,
    mode=mode)

if mode == ModeKeys.PREDICT:
    aggregator = training_utils_v1.OutputsAggregator(
        True, steps=steps_per_epoch)
else:
    aggregator = training_utils_v1.MetricsAggregator(
        True, steps=steps_per_epoch)

should_set_learning_phase = context.executing_eagerly() and model.run_eagerly
if should_set_learning_phase:
    learning_phase_scope = backend.eager_learning_phase_scope(
        1 if mode == ModeKeys.TRAIN else 0)
    learning_phase_scope.__enter__()

callbacks.model.stop_training = False
callbacks._call_begin_hook(mode)

initial_epoch = model._maybe_load_initial_epoch_from_ckpt(initial_epoch, mode)

for epoch in range(initial_epoch, epochs):
    if callbacks.model.stop_training:
        break

    # Setup work for each epoch.
    model.reset_metrics()
    epoch_logs = {}
    if mode == ModeKeys.TRAIN:
        callbacks.on_epoch_begin(epoch, epoch_logs)

    if steps_per_epoch is None:
        # Loop over dataset until `OutOfRangeError` is raised.
        target_steps = np.inf
    else:
        # Loop over dataset for the specified number of steps.
        target_steps = steps_per_epoch

    step = 0
    while step < target_steps:
        batch_data = _get_next_batch(generator)
        if batch_data is None:
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

        # `batch_size` used for validation data if validation
        # data is NumPy/EagerTensors.
        batch_size = int(nest.flatten(batch_data)[0].shape[0])

        # Callbacks batch begin.
        batch_logs = {'batch': step, 'size': batch_size}
        callbacks._call_batch_hook(mode, 'begin', step, batch_logs)

        is_deferred = not model._is_compiled
        batch_outs = batch_function(*batch_data)
        if not isinstance(batch_outs, list):
            batch_outs = [batch_outs]

        if step == 0:
            aggregator.create(batch_outs)

            if is_deferred:
                # Set callbacks params. We do this here when model is compiled only
                # in the first iteration of this loop (deferred build scenario).
                cbks.set_callback_parameters(
                    callbacks,
                    model,
                    do_validation=do_validation,
                    batch_size=batch_size,
                    epochs=epochs,
                    steps_per_epoch=steps_per_epoch,
                    samples=num_samples_or_steps,
                    verbose=verbose,
                    mode=mode)

      # Aggregate results.
        aggregator.aggregate(batch_outs)

        # Callbacks batch end.
        batch_logs = cbks.make_logs(model, batch_logs, batch_outs, mode)
        callbacks._call_batch_hook(mode, 'end', step, batch_logs)
        step += 1

        if callbacks.model.stop_training:
            break

    aggregator.finalize()
    results = aggregator.results
    epoch_logs = cbks.make_logs(model, epoch_logs, results, mode)
    if len(results) == 1:
        results = results[0]

    # Run the test loop every epoch during training.
    if (do_validation and
        training_utils_v1.should_run_validation(validation_freq, epoch) and
        not callbacks.model.stop_training):
        val_results = model_iteration(
            model,
            validation_data,
            steps_per_epoch=validation_steps,
            batch_size=batch_size,
            class_weight=class_weight,
            workers=workers,
            use_multiprocessing=use_multiprocessing,
            max_queue_size=max_queue_size,
            callbacks=callbacks,
            verbose=verbose,
            mode=ModeKeys.TEST,
            steps_name='validation_steps')

        if not isinstance(val_results, list):
            val_results = [val_results]
        epoch_logs = cbks.make_logs(
            model, epoch_logs, val_results, mode, prefix='val_')

    if mode == ModeKeys.TRAIN:
        # Epochs only apply to `fit`.
        callbacks.on_epoch_end(epoch, epoch_logs)

    # Recreate dataset iterator for the next epoch.
    if reset_dataset_after_each_epoch and epoch < epochs - 1:
        generator = dataset_ops.make_one_shot_iterator(original_dataset)

model._successful_loop_finish = True
callbacks._call_end_hook(mode)

if enqueuer is not None:
    enqueuer.stop()

if should_set_learning_phase:
    learning_phase_scope.__exit__(None, None, None)

if mode == ModeKeys.TRAIN:
    exit(model.history)
exit(results)
