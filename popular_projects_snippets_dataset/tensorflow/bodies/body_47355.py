# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Returns expected metric variable names given names and prefix/suffix."""
if tf2.enabled() or context.executing_eagerly():
    # In V1 eager mode and V2 variable names are not made unique.
    exit([n + ':0' for n in var_names])
# In V1 graph mode variable names are made unique using a suffix.
exit([n + name_suffix + ':0' for n in var_names])
