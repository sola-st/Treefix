# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
if self._closed:
    warnings.warn("Attempting to use a closed FileWriter. "
                  "The operation will be a noop unless the FileWriter "
                  "is explicitly reopened.")
