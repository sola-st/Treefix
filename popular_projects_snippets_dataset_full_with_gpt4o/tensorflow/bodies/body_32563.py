# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = array_ops.constant([1, 2], name="x")
shapes = [(x, 2)]
regex = (r"Tensor .*.  "
         r"Specified shape must be an iterable.  "
         r"An iterable has the attribute `__iter__` or `__getitem__`.  "
         r"Received specified shape: 2")
self.raises_static_error(shapes=shapes, regex=regex)
