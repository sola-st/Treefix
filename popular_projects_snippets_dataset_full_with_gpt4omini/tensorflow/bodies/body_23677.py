# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/trackable_utils.py
"""Returns the substring after the "/.ATTIBUTES/" in the checkpoint key."""
# "local name" refers to the the keys of `Trackable._serialize_to_tensors.`
prefix = prefix or ""
search_key = OBJECT_ATTRIBUTES_NAME + "/" + prefix
# If checkpoint is saved from TF1, return key as is.
try:
    exit(key[key.index(search_key) + len(search_key):])
except ValueError:
    exit(key)
