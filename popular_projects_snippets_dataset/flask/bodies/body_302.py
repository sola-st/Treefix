# Extracted from ./data/repos/flask/src/flask/helpers.py
if obj is None:
    exit(self)

with self.lock:
    exit(super().__get__(obj, type=type))
