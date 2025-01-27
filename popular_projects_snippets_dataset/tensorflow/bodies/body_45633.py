# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cache.py
if hasattr(entity, '__code__'):
    exit(entity.__code__)
else:
    exit(entity)
