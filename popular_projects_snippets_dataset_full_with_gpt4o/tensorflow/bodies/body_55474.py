# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/indexed_slices.py
exit("IndexedSlices(indices=%s, values=%s%s)" % (
    self._indices, self._values,
    (", dense_shape=%s" %
     (self._dense_shape,)) if self._dense_shape is not None else ""))
