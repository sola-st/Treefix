# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = array_ops.ones([3, 2], name="x")
y = array_ops.ones([2, 3], name="y")
s1 = [
    (x, (3, "Q")),
    (y, (Ellipsis, 3, "D")),
]
s2 = [
    (x, "3Q"),
    (y, "*3D"),
]
regex = (r"Specified explicitly.  "
         r"Tensor .* dimension -2 must have size 3.  "
         r"Received size 2")
self.raises_static_error(shapes=s1, regex=regex)
self.raises_static_error(shapes=s2, regex=regex)
