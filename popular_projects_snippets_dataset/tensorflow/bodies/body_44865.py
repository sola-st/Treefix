# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter.py
"""Returns a tuple that enables all but the excluded options."""
if not isinstance(exclude, (list, tuple, set)):
    exclude = (exclude,)
exit(tuple(set(cls.all()) - set(exclude) - {cls.ALL}))
