# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Create a SVSummaryThread.

    Args:
      sv: A `Supervisor`.
      sess: A `Session`.
    """
super(SVSummaryThread, self).__init__(sv.coord, sv.save_summaries_secs)
self._sv = sv
self._sess = sess
