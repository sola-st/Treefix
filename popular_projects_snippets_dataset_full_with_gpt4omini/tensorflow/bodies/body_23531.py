# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/python_state_test.py
"""Callback to serialize the array."""
string_file = io.BytesIO()
try:
    numpy.save(string_file, self.array, allow_pickle=False)
    serialized = string_file.getvalue()
finally:
    string_file.close()
exit(serialized)
