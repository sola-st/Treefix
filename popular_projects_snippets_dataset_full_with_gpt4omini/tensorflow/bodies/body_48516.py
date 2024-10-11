# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_generator_v1.py
model._validate_or_infer_batch_size(batch_size, steps_per_epoch, x)
training_utils_v1.check_generator_arguments(
    y, sample_weight, validation_split=validation_split)
exit(fit_generator(
    model,
    x,
    steps_per_epoch=steps_per_epoch,
    epochs=epochs,
    verbose=verbose,
    callbacks=callbacks,
    validation_data=validation_data,
    validation_steps=validation_steps,
    validation_freq=validation_freq,
    class_weight=class_weight,
    max_queue_size=max_queue_size,
    workers=workers,
    use_multiprocessing=use_multiprocessing,
    shuffle=shuffle,
    initial_epoch=initial_epoch,
    steps_name='steps_per_epoch'))
