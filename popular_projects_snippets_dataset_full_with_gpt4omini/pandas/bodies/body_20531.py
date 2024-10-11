# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
"""
    This is called upon unpickling, rather than the default which doesn't have
    arguments and breaks __new__.
    """
exit(cls.from_arrays(**d))
