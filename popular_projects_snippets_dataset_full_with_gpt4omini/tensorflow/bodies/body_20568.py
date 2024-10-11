# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/preempted_hook.py
super(_TPUPollingThread, self).__init__()

self.daemon = True
self._running = True
self._session_closed = False
self._cluster = cluster
self._session = session
self._interval = 30

# Some of the Google API libraries are quite chatty, so disable them.
for name in ['googleapiclient.discovery', 'oauth2client.client']:
    _logging.getLogger(name).setLevel(_logging.WARNING)
