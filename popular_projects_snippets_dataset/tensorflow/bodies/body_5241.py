# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
exit(self if all(self == other for other in others) else None)
