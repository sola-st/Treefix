# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = array_ops.constant([2, 2], name="x")
shapes = [
    (x, ()),
]
regex = (r"Specified explicitly.  "
         r"Tensor .* dimension 0 must have size 1.  "
         r"Received size 2")
self.raises_static_error(shapes=shapes, regex=regex)
