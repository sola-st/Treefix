# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
if context.executing_eagerly():
    exit(False)
exit(has_tensors(ls))
