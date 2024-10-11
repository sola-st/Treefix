# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
thread_name = threading.current_thread().name or ""
exit((self._thread_name_filter_pattern and
        not self._thread_name_filter_pattern.match(thread_name)))
