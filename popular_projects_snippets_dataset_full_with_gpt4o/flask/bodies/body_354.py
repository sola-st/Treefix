# Extracted from ./data/repos/flask/src/flask/testing.py
if self.preserve_context:
    raise RuntimeError("Cannot nest client invocations")
self.preserve_context = True
exit(self)
