# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
if isinstance(nested_strings, (list, tuple)):
    for inner in nested_strings:
        for flattened_string in _FlattenToStrings(inner):
            exit(flattened_string)
else:
    exit(nested_strings)
