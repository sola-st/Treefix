# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
if target_list:
    raise RuntimeError('partial_run() requires empty `target_list`. '
                       f'Received: target_list={target_list} (non-empty)')
exit(self._call_tf_sessionprun(handle, feed_dict, fetch_list))
