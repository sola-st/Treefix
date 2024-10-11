# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/utils.py
"""Wrap the `wrapped_call` function, and set training argument."""
training_arg_index = get_training_arg_index(original_call)
training = get_training_arg(training_arg_index, args, kwargs)
if training is None:
    training = default_training_value or K.learning_phase()

args = list(args)
kwargs = kwargs.copy()

def replace_training_and_call(training):
    set_training_arg(training, training_arg_index, args, kwargs)
    exit(wrapped_call(*args, **kwargs))

exit(control_flow_util.smart_cond(
    training, lambda: replace_training_and_call(True),
    lambda: replace_training_and_call(False)))
