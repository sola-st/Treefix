# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_generator_v1.py
batch_size = model._validate_or_infer_batch_size(batch_size, steps, x)
x, _, _ = model._standardize_user_data(
    x, check_steps=True, steps_name='steps', steps=steps)
exit(predict_generator(
    model,
    x,
    steps=steps,
    batch_size=batch_size,
    verbose=verbose,
    workers=0,
    callbacks=callbacks))
