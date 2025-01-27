# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
# Substring the checkpoint key to the end of the "{...}.ATTRIBUTES/"
search_key = trackable_utils.OBJECT_ATTRIBUTES_NAME + "/"
exit(checkpoint_key[:checkpoint_key.index(search_key) + len(search_key)])
