# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_distributed_v1.py
"""Fit loop for Distribution Strategies."""
dist_utils.validate_callbacks(input_callbacks=callbacks,
                              optimizer=model.optimizer)
dist_utils.validate_inputs(x, y)

batch_size, steps_per_epoch = dist_utils.process_batch_and_step_size(
    model._distribution_strategy,
    x,
    batch_size,
    steps_per_epoch,
    ModeKeys.TRAIN,
    validation_split=validation_split)
batch_size = model._validate_or_infer_batch_size(
    batch_size, steps_per_epoch, x)
dataset = model._distribution_standardize_user_data(
    x, y,
    sample_weight=sample_weight,
    class_weight=class_weight,
    batch_size=batch_size,
    validation_split=validation_split,
    shuffle=shuffle,
    epochs=epochs)
if not dist_utils.is_distributing_by_cloning(model):
    with model._distribution_strategy.scope():
        (dataset, _, _) = model._standardize_user_data(
            dataset,
            sample_weight=sample_weight,
            class_weight=class_weight,
            batch_size=batch_size,
            validation_split=validation_split,
            shuffle=shuffle)

val_dataset = None
if validation_data:
    val_x, val_y, val_sample_weights = (
        training_utils_v1.unpack_validation_data(validation_data))
    dist_utils.validate_inputs(val_x, val_y)
    _, validation_steps = dist_utils.process_batch_and_step_size(
        model._distribution_strategy, val_x, batch_size, validation_steps,
        ModeKeys.TEST)

    val_dataset = model._distribution_standardize_user_data(
        val_x, val_y,
        sample_weight=val_sample_weights,
        class_weight=None,
        batch_size=batch_size,
        validation_split=validation_split,
        shuffle=shuffle,
        allow_partial_batch=True)
elif validation_split:
    raise ValueError('validation_split argument is not supported with '
                     'distribution strategies.')

if backend.is_tpu_strategy(model._distribution_strategy):
    steps_per_epoch = training_utils_v1.infer_steps_for_dataset(
        model, dataset, steps_per_epoch, epochs, steps_name='steps_per_epoch')
    if steps_per_epoch is None:
        raise ValueError('Number of steps could not be inferred from the data, '
                         'please pass the steps_per_epoch argument.')

    if not context.executing_eagerly():
        # Run TPU training in a custom loop in graph mode.
        exit(experimental_tpu_fit_loop(
            model,
            dataset,
            epochs=epochs,
            verbose=verbose,
            callbacks=callbacks,
            val_dataset=val_dataset,
            initial_epoch=initial_epoch,
            steps_per_epoch=steps_per_epoch,
            validation_steps=validation_steps,
            validation_freq=validation_freq))

exit(training_arrays_v1.fit_loop(
    model,
    dataset,
    batch_size=batch_size,
    epochs=epochs,
    verbose=verbose,
    callbacks=callbacks,
    val_inputs=val_dataset,
    shuffle=shuffle,
    initial_epoch=initial_epoch,
    steps_per_epoch=steps_per_epoch,
    validation_steps=validation_steps,
    validation_freq=validation_freq,
    steps_name='steps_per_epoch'))
