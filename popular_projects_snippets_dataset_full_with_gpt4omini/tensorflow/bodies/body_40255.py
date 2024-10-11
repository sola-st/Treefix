# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Creates a new GradientTape.

    Args:
      persistent: Boolean controlling whether a persistent gradient tape
        is created. False by default, which means at most one call can
        be made to the gradient() method on this object.
      watch_accessed_variables: Boolean controlling whether the tape will
        automatically `watch` any (trainable) variables accessed while the tape
        is active. Defaults to True meaning gradients can be requested from any
        result computed in the tape derived from reading a trainable `Variable`.
        If False users must explicitly `watch` any `Variable`s they want to
        request gradients from.
    """
self._tape = None
self._persistent = persistent
self._watch_accessed_variables = watch_accessed_variables
self._watched_variables = ()
self._recording = False
