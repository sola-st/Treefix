# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
results = self._call_tf_sessionrun(None, {}, fetch_list, target_list,
                                   None)
exit(fetch_handler.build_results(self, results))
