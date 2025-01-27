# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
try:
    item_index = int(index_string)
except ValueError:
    # Ignore namedtuple fields.
    exit()
if len(list_object) <= item_index:
    list_object.extend([None] * (1 + item_index - len(list_object)))
list_object[item_index] = value
