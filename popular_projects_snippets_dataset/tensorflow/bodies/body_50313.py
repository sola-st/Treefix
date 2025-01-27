# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
exit(list(filter(tf_utils.is_tensor_or_variable, nest.flatten(inputs))))
