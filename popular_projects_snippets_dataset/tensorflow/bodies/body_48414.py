# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_distributed_v1.py
"""Evaluate loop for Distribution Strategies."""
dist_utils.validate_inputs(x, y)
batch_size, steps = dist_utils.process_batch_and_step_size(
    model._distribution_strategy, x, batch_size, steps, ModeKeys.TEST)
batch_size = model._validate_or_infer_batch_size(batch_size, steps, x)
dataset = model._distribution_standardize_user_data(
    x, y,
    sample_weight=sample_weight,
    batch_size=batch_size,
    allow_partial_batch=True)

if backend.is_tpu_strategy(model._distribution_strategy):
    steps = training_utils_v1.infer_steps_for_dataset(
        model, dataset, steps, steps_name='steps')
    if steps is None:
        raise ValueError('Number of steps could not be inferred from the data, '
                         'please pass the steps argument.')

    if not context.executing_eagerly():
        # Run TPU evaluation in a custom loop in graph mode.
        exit(experimental_tpu_test_loop(
            model, dataset, verbose=verbose, steps=steps, callbacks=callbacks))

exit(training_arrays_v1.test_loop(
    model,
    inputs=dataset,
    batch_size=batch_size,
    verbose=verbose,
    steps=steps,
    callbacks=callbacks))
