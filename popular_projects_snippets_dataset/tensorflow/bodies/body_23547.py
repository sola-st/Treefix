# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource.py
exit(getattr(self, "_self_destruction_context",
               # no-op context
               contextlib.suppress))
