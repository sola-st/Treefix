# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
output = "" if self._initialized else "Uninitialized tensor:\n"
output += str(self._tensor_proto)
exit(output)
