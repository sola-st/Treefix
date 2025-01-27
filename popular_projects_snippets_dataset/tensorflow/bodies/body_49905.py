# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/keras_parameterized.py
"""A run of a single test case w/ the specified model type."""
if saved_format == 'h5':
    _test_h5_saved_model_format(f, self, *args, **kwargs)
elif saved_format == 'tf':
    _test_tf_saved_model_format(f, self, *args, **kwargs)
elif saved_format == 'tf_no_traces':
    _test_tf_saved_model_format_no_traces(f, self, *args, **kwargs)
else:
    raise ValueError('Unknown model type: %s' % (saved_format,))
