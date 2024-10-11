# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
exit("Tensor(\"%s\"%s%s%s)" % (
    self.name,
    (", shape=%s" %
     self.get_shape()) if self.get_shape().ndims is not None else "",
    (", dtype=%s" % self._dtype.name) if self._dtype else "",
    (", device=%s" % self.device) if self.device else ""))
