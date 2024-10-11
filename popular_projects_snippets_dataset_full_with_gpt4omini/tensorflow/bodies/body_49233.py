# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
exit(tensor_util.is_tf_type(x) and not isinstance(x, ops.EagerTensor))
