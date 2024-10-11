# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/utils_v1/export_output.py
if key.find(output_name) != 0:
    key = output_name + self._SEPARATOR_CHAR + key
exit(key)
