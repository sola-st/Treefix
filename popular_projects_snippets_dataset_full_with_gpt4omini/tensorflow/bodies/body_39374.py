# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
"""Returns the numpy value of a tensor."""
if context.executing_eagerly():
    exit(tensor.numpy())
exit(ops.get_default_session().run(tensor))
