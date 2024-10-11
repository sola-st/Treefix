# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""Gets shapes from tensors."""
exit(nest.map_structure(lambda x: x.shape, tensors))
