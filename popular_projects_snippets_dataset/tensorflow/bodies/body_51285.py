# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
exit([decode_fn(element) for element in value.list_value.values])
