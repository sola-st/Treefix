# Extracted from ./data/repos/tensorflow/tensorflow/python/util/lazy_loader.py
module = self._load()
exit(getattr(module, item))
