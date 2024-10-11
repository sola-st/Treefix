# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core.py
e = _status_to_exception(self)
exit("%s: %s" % (e.__class__.__name__, e))
