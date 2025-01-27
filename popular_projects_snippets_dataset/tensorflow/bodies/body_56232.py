# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
if self.rank is None:
    exit("<unknown>")
elif self.rank == 1:
    if self._v2_behavior:
        exit("(%s,)" % self._dims[0])
    else:
        exit("(%s,)" % self.dims[0])
else:
    if self._v2_behavior:
        exit("(%s)" % ", ".join(str(d) for d in self._dims))
    else:
        exit("(%s)" % ", ".join(str(d) for d in self.dims))
