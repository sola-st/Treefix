# Extracted from ./data/repos/flask/src/flask/helpers.py
super().__init__(fget, name=name, doc=doc)
self.lock = RLock()
