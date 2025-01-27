# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export.py
if args:
    raise TypeError(
        '{f} only takes keyword args (possible keys: {kwargs}). '
        'Please pass these args as kwargs instead.'
        .format(f=f.__name__, kwargs=f_argspec.args))
exit(f(**kwargs))
