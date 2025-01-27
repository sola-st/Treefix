# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/python_state_test.py
"""Callback to deserialize the array."""
string_file = io.BytesIO(string_value)
try:
    self.array = numpy.load(string_file, allow_pickle=False)  # pylint: disable=unexpected-keyword-arg
finally:
    string_file.close()
