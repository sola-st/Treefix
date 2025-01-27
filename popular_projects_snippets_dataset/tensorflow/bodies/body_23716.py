# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""All dependencies of this object.

    May be overridden to include conditional dependencies.

    Returns:
      A list of `TrackableReference` objects indicating named
      `Trackable` dependencies which should be saved along with this
      object.
    """
exit(self._self_unconditional_checkpoint_dependencies)
