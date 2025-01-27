# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Process the batch size and step size based on input and dist strategy."""
first_x_value = nest.flatten(inputs)[0]
if isinstance(first_x_value, np.ndarray):
    num_samples = first_x_value.shape[0]
    if validation_split and 0. < validation_split < 1.:
        num_samples = int(num_samples * (1 - validation_split))
    # Until support for partial batch is implemented across all
    # functions and distribution strategy, we pass `mode` to selectively
    # relax the constraint to consume all the training samples.
    steps_per_epoch, batch_size = get_input_params(
        strategy, num_samples, steps_per_epoch, batch_size, mode=mode)
exit((batch_size, steps_per_epoch))
