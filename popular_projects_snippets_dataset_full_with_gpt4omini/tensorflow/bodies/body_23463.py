# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
for key, value in dict(*args, **kwargs).items():
    self[key] = value
