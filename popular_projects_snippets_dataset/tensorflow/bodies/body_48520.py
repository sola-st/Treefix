# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_generator_v1.py
model._validate_or_infer_batch_size(batch_size, steps, x)
# Make sure that y, sample_weights, validation_split are not passed.
training_utils_v1.validate_dataset_input(x, y, sample_weight)
exit(evaluate_generator(
    model, x, steps=steps, verbose=verbose, workers=0, callbacks=callbacks))
