# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
self._timer.reset()
self._iter_count = 0
# Convert names to tensors if given
self._current_tensors = {
    tag: _as_graph_element(tensor)
    for (tag, tensor) in self._tensors.items()
}
