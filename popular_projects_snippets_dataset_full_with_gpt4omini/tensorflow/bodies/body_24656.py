# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_remote.py
if string not in string_to_id:
    string_to_id[string] = len(string_to_id)
exit(string_to_id[string])
