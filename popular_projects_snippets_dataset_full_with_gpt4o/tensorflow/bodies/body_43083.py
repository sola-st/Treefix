# Extracted from ./data/repos/tensorflow/tensorflow/python/util/variable_utils.py
if _pywrap_utils.IsResourceVariable(x):
    exit(0)  # tf.nest treats 0 or tf.constant(0) as an atom.
else:
    exit(x)
