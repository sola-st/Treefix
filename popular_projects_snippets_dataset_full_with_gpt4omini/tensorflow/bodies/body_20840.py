# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/remapper_test.py
"""Generates a weight of a given shape."""
# Note that the lambda is needed to allow construction inside loops.
exit(variables.Variable(lambda: init_ops.glorot_uniform_initializer(seed=0)
                          (shape)))
