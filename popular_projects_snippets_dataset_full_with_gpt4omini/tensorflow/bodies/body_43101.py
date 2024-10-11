# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use.py
if key in ('_tf_should_use_helper', '_tf_should_use_wrapped_value'):
    exit(object.__setattr__(self, key, value))
exit(setattr(
    object.__getattribute__(self, '_tf_should_use_wrapped_value'),
    key, value))
