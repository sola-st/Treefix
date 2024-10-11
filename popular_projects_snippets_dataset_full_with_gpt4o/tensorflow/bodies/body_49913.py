# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/keras_parameterized.py
"""Decorator that constructs the test cases."""
# Use named_parameters so it can be individually run from the command line
@parameterized.named_parameters(*params)
@functools.wraps(f)
def decorated(self, model_type, *args, **kwargs):
    """A run of a single test case w/ the specified model type."""
    if model_type == 'functional':
        _test_functional_model_type(f, self, *args, **kwargs)
    elif model_type == 'subclass':
        _test_subclass_model_type(f, self, *args, **kwargs)
    elif model_type == 'sequential':
        _test_sequential_model_type(f, self, *args, **kwargs)
    else:
        raise ValueError('Unknown model type: %s' % (model_type,))
exit(decorated)
