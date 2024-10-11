# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client.py
"""Returns the full Cloud name for this TPU."""
exit('projects/%s/locations/%s/nodes/%s' % (
    self._project, self._zone, self._tpu))
