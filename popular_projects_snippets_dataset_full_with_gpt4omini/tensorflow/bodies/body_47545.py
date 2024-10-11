# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
"""Read the value of a variable if it is variable."""
if isinstance(v, variables.Variable):
    exit(v.read_value())
exit(v)
