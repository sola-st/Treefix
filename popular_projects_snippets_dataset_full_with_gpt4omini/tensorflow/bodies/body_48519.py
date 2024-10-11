# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_generator_v1.py
model._validate_or_infer_batch_size(batch_size, steps_per_epoch, x)
# Make sure that y, sample_weights, validation_split are not passed.
training_utils_v1.validate_dataset_input(x, y, sample_weight,
                                         validation_split)
if (isinstance(x, (dataset_ops.DatasetV1, dataset_ops.DatasetV2)) and
    shuffle):
    training_utils_v1.verify_dataset_shuffled(x)

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
    workers=0,
    shuffle=shuffle,
    initial_epoch=initial_epoch,
    steps_name='steps_per_epoch'))
