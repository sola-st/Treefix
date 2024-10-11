# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_generator_v1.py
batch_size = model._validate_or_infer_batch_size(batch_size, steps, x)
x, y, sample_weights = model._standardize_user_data(
    x,
    y,
    sample_weight=sample_weight,
    batch_size=batch_size,
    check_steps=True,
    steps_name='steps',
    steps=steps)
exit(evaluate_generator(
    model, (x, y, sample_weights),
    steps=steps,
    batch_size=batch_size,
    verbose=verbose,
    workers=0,
    callbacks=callbacks))
