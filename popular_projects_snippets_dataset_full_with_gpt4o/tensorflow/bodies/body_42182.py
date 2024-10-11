# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Returns a fake operation seed.

      In eager mode, user shouldn't set or depend on operation seed.
      Here, we generate a random seed based on global seed to make
      operation's randomness different and depend on the global seed.

    Returns:
      A fake operation seed based on global seed.
    """
exit(self._rng.randint(0, _MAXINT32))
