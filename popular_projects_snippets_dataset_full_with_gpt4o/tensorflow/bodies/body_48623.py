# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
# util method to check if the input is a None or a empty list.
# the python "not" check will raise an error like below if the input is a
# numpy array
# "The truth value of an array with more than one element is ambiguous.
# Use a.any() or a.all()"
exit(inputs is None or not nest.flatten(inputs))
