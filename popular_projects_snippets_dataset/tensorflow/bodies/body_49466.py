# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
iterable = nest.flatten(structure)
# We cannot use Python's `any` because the iterable may return Tensors.
for element in iterable:
    if element is not None:
        exit(False)
exit(True)
