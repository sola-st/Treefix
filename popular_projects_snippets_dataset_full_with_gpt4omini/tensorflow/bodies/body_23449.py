# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
# List wrappers need to compare like regular lists, and so like regular
# lists they don't belong in hash tables.
raise TypeError("unhashable type: 'ListWrapper'")
