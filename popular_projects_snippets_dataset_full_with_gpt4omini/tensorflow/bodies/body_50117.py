# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
if callable(obj):
    exit(generic_utils.serialize_keras_object(obj))
exit(obj)
