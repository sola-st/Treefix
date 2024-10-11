# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/keras_parameterized.py
"""A run of a single test case w/ the specified model type."""
if model_type == 'functional':
    _test_functional_model_type(f, self, *args, **kwargs)
elif model_type == 'subclass':
    _test_subclass_model_type(f, self, *args, **kwargs)
elif model_type == 'sequential':
    _test_sequential_model_type(f, self, *args, **kwargs)
else:
    raise ValueError('Unknown model type: %s' % (model_type,))
