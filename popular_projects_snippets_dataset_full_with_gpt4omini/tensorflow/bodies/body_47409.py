# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
"""Create the cache for dropout and recurrent dropout mask.

    Note that the following two masks will be used in "graph function" mode,
    e.g. these masks are symbolic tensors. In eager mode, the `eager_*_mask`
    tensors will be generated differently than in the "graph function" case,
    and they will be cached.

    Also note that in graph mode, we still cache those masks only because the
    RNN could be created with `unroll=True`. In that case, the `cell.call()`
    function will be invoked multiple times, and we want to ensure same mask
    is used every time.

    Also the caches are created without tracking. Since they are not picklable
    by python when deepcopy, we don't want `layer._obj_reference_counts_dict`
    to track it by default.
    """
self._dropout_mask_cache = backend.ContextValueCache(
    self._create_dropout_mask)
self._recurrent_dropout_mask_cache = backend.ContextValueCache(
    self._create_recurrent_dropout_mask)
