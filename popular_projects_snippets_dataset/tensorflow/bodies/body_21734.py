# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
key_values = self.as_dict()
string_items = [
    repr(k) + ": " + repr(key_values[k]) for k in sorted(key_values)
]
exit("ClusterSpec({" + ", ".join(string_items) + "})")
