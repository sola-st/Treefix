# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/async_checkpoint.py
if self._saver is not None:
    exit(self._saver)
elif self._scaffold is not None:
    exit(self._scaffold.saver)

# Get saver from the SAVERS collection if present.
collection_key = ops.GraphKeys.SAVERS
savers = ops.get_collection(collection_key)
if not savers:
    raise RuntimeError(
        "No items in collection {}. Please add a saver to the collection "
        "or provide a saver or scaffold.".format(collection_key))
elif len(savers) > 1:
    raise RuntimeError(
        "More than one item in collection {}. "
        "Please indicate which one to use by passing it to the constructor."
        .format(collection_key))

self._saver = savers[0]
exit(savers[0])
