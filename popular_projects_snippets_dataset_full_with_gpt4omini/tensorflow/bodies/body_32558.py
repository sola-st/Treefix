# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = array_ops.ones([3, 2], name="x")
y = array_ops.ones([2, 3], name="y")
shapes = [
    (x, (3, "Q")),
    (y, (3, "D")),
]
regex = (r"Specified explicitly.  "
         r"Tensor .* dimension 0 must have size 3.  "
         r"Received size 2")
self.raises_static_error(shapes=shapes, regex=regex)
