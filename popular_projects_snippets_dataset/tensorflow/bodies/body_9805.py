# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
# Register a dead handle in the session. Delete the dead tensors when
# the number of dead tensors exceeds certain threshold.
tensors_to_delete = None
with self._delete_lock:
    self._dead_handles.append(handle)
    if len(self._dead_handles) == BaseSession._DEAD_HANDLES_THRESHOLD:
        tensors_to_delete = self._dead_handles
        self._dead_handles = []
    # Delete the dead tensors.
if tensors_to_delete:
    feeds = {}
    fetches = []
    for deleter_key, tensor_handle in enumerate(tensors_to_delete):
        holder, deleter = session_ops._get_handle_deleter(
            self.graph, deleter_key, tensor_handle)
        feeds[holder] = tensor_handle
        fetches.append(deleter)
    self.run(fetches, feed_dict=feeds)
