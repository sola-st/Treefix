# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
results = self._call_tf_sessionrun(None, {}, fetch_list, [], None)
exit(results[0])
