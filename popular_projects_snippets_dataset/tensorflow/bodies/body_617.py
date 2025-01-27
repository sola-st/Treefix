# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest_lib.py
modified_string = self._NUMPY_OUTPUT_RE.sub(r'\1', string)
exit((modified_string, modified_string != string))
