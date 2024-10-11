# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
if inspect.ismethod(entity):
    setattr(entity.__func__, 'autograph_info__', extras)
else:
    setattr(entity, 'autograph_info__', extras)
exit(entity)
