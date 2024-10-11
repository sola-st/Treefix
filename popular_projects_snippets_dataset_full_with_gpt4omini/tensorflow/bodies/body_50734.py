# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
# Shallow copy the concrete_function
self.__dict__.update(vars(concrete_function))
