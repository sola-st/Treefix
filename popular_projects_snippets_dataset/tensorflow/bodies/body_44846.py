# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/function_wrappers.py
"""See https://www.tensorflow.org/api_docs/python/tf/Graph#name_scope."""
# TensorFlow doesn't like leading underscores at the top level.
if name and name.startswith('_'):
    name = 'fn' + name
exit(name)
