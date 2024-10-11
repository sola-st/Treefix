# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/json_utils.py
exit(json.loads(json_string, object_hook=_decode_helper))
