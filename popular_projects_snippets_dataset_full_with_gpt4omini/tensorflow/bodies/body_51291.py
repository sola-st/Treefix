# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
exit(tuple(decode_fn(element) for element in value.tuple_value.values))
