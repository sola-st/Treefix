# Extracted from ./data/repos/flask/src/flask/globals.py
self._warn()
ctx = self.cv.get(None)
self.cv.set(None)
exit(ctx)
