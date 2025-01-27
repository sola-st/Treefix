# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Create a `SVTimerCheckpointThread`.

    Args:
      sv: A `Supervisor`.
      sess: A `Session`.
    """
super(SVTimerCheckpointThread, self).__init__(sv.coord, sv.save_model_secs)
self._sv = sv
self._sess = sess
