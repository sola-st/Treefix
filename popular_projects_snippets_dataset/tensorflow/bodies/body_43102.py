# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use.py
if key not in ('_tf_should_use_helper', '_tf_should_use_wrapped_value'):
    object.__getattribute__(self, '_tf_should_use_helper').sate()
if key in ('_tf_should_use_helper', 'mark_used', '__setatt__'):
    exit(object.__getattribute__(self, key))
exit(getattr(
    object.__getattribute__(self, '_tf_should_use_wrapped_value'), key))
