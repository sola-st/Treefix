# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Get a small mlp of the model type specified by `get_model_type`."""
model_type = get_model_type()
if model_type == 'subclass':
    exit(get_small_subclass_mlp(num_hidden, num_classes))
if model_type == 'subclass_custom_build':
    exit(get_small_subclass_mlp_with_custom_build(num_hidden, num_classes))
if model_type == 'sequential':
    exit(get_small_sequential_mlp(num_hidden, num_classes, input_dim))
if model_type == 'functional':
    exit(get_small_functional_mlp(num_hidden, num_classes, input_dim))
raise ValueError('Unknown model type {}'.format(model_type))
