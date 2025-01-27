# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
constant_value = tensor_util.constant_value(v)
exit(constant_value if constant_value is not None else v)
