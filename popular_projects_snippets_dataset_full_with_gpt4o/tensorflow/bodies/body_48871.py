# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_arrays_v1.py
batch_size = model._validate_or_infer_batch_size(batch_size,
                                                 steps_per_epoch, x)

x, y, sample_weights = model._standardize_user_data(
    x,
    y,
    sample_weight=sample_weight,
    class_weight=class_weight,
    batch_size=batch_size,
    check_steps=True,
    steps_name='steps_per_epoch',
    steps=steps_per_epoch,
    validation_split=validation_split,
    shuffle=shuffle)

if validation_data:
    val_x, val_y, val_sample_weights = model._prepare_validation_data(
        validation_data, batch_size, validation_steps)
elif validation_split and 0. < validation_split < 1.:
    (x, y, sample_weights, val_x, val_y, val_sample_weights
    ) = training_utils_v1.split_training_and_validation_data(
        x, y, sample_weights, validation_split)
else:
    if validation_steps:
        raise ValueError('`validation_steps` should not be specified if '
                         '`validation_data` is None.')
    val_x, val_y, val_sample_weights = None, None, None

exit(fit_loop(
    model,
    inputs=x,
    targets=y,
    sample_weights=sample_weights,
    batch_size=batch_size,
    epochs=epochs,
    verbose=verbose,
    callbacks=callbacks,
    val_inputs=val_x,
    val_targets=val_y,
    val_sample_weights=val_sample_weights,
    shuffle=shuffle,
    initial_epoch=initial_epoch,
    steps_per_epoch=steps_per_epoch,
    validation_steps=validation_steps,
    validation_freq=validation_freq,
    steps_name='steps_per_epoch'))
