# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors.py
super(InfNanMonitor, self).__init__(debug_events_reader)
self._limit = limit  # Track only the first _ alert events, for efficiency.
self._alerts = []
