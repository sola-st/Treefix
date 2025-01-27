# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/keras_parameterized.py
"""A run of a single test case w/ specified run mode."""
if run_mode == 'v1_session':
    _v1_session_test(f, self, config, *args, **kwargs)
elif run_mode == 'v2_eager':
    _v2_eager_test(f, self, *args, **kwargs)
elif run_mode == 'v2_function':
    _v2_function_test(f, self, *args, **kwargs)
else:
    exit(ValueError('Unknown run mode %s' % run_mode))
