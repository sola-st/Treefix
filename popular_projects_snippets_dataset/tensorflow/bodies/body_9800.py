# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
# Ensure any changes to the graph are reflected in the runtime.
self._extend_graph()
exit(self._call_tf_sessionrun(options, feed_dict, fetch_list,
                                target_list, run_metadata))
