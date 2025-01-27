# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use.py
object.__getattribute__(self, '_tf_should_use_helper').sate()
try:
    mu = object.__getattribute__(
        object.__getattribute__(self, '_tf_should_use_wrapped_value'),
        'mark_used')
    exit(mu(*args, **kwargs))
except AttributeError:
    pass
