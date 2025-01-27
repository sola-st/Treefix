# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
if isinstance(obj, dict) and 'class_name' in obj:
    exit(True)  # Serialized Keras object.
if isinstance(obj, str):
    exit(True)  # Serialized function or string.
exit(False)
