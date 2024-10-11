# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
exit({key: decode_fn(val) for key, val in value.dict_value.fields.items()})
