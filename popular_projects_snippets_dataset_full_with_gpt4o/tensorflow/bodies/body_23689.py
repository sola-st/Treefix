# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
if isinstance(o, tuple):
    exit((self.name, self.ref) == o)
elif isinstance(o, TrackableReference):
    exit(self.name == o.name and self.ref == o.ref)
else:
    exit(False)
