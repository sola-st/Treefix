# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager.py
diff = self._duration_secs - (time.time() - self._start_time_secs)
exit(max(0, diff))
