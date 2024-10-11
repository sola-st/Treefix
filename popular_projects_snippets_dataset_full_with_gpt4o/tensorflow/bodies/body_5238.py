# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
exit(hash((self.name, self.graph, tuple(self.traceback), self.type)))
