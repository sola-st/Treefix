# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/trackable_utils.py
"""Substrings the checkpoint key to the start of "/.ATTRIBUTES"."""
search_key = "/" + OBJECT_ATTRIBUTES_NAME
exit(key[:key.index(search_key)])
