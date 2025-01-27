# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_arrays_v1.py
batch_size = model._validate_or_infer_batch_size(batch_size, steps, x)
x, _, _ = model._standardize_user_data(
    x, check_steps=True, steps_name='steps', steps=steps)
exit(predict_loop(
    model,
    x,
    batch_size=batch_size,
    verbose=verbose,
    steps=steps,
    callbacks=callbacks))
