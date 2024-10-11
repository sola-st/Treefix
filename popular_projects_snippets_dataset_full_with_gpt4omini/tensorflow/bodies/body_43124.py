# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
exit(any(
    isinstance(x, TensorTracer)
    for x in self._flatten_with_slice_flattening(value)))
