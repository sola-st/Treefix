# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
exit(tf_session.TF_SessionRun_wrapper(self._session, options, feed_dict,
                                        fetch_list, target_list,
                                        run_metadata))
