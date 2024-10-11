# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cache.py
if inspect.ismethod(entity):
    exit(entity.__func__)
exit(entity)
