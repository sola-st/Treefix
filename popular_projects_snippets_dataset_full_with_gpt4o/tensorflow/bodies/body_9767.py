# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Creates a fetch handler.

    Args:
      graph: Graph of the fetches.   Used to check for fetchability and to
        convert all fetches to tensors or ops as needed.
      fetches: An arbitrary fetch structure: singleton, list, tuple, namedtuple,
        or dict.
      feeds: A feed dict where keys are Tensors.
      feed_handles: A dict from feed Tensors to TensorHandle objects used as
        direct feeds.
    """
with graph.as_default():
    self._fetch_mapper = _FetchMapper.for_fetch(fetches)
self._fetches = []
self._targets = []
self._feeds = feeds
self._feed_handles = feed_handles or {}
self._ops = []
self._fetch_handles = {}
for fetch in self._fetch_mapper.unique_fetches():
    if isinstance(fetch, ops.Operation):
        self._assert_fetchable(graph, fetch)
        self._targets.append(fetch)
        self._ops.append(True)
    else:
        self._assert_fetchable(graph, fetch.op)
        self._fetches.append(fetch)
        self._ops.append(False)
    # Remember the fetch if it is for a tensor handle.
    if (isinstance(fetch, ops.Tensor) and
        (fetch.op.type == 'GetSessionHandle' or
         fetch.op.type == 'GetSessionHandleV2')):
        self._fetch_handles[fetch.ref()] = fetch.op.inputs[0].dtype
self._final_fetches = [x for x in self._fetches if x.ref() not in feeds]
