# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = array_ops.ones([3, 2], name="x")
y = array_ops.ones([2, 3], name="y")
shapes = [
    (x, ("N", "Q")),
    (y, ("N", "D")),
]
regex = (r"Specified by tensor .* dimension 0.  "
         r"Tensor .* dimension 0 must have size 3.  "
         r"Received size 2")
self.raises_static_error(shapes=shapes, regex=regex)
