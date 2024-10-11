# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = array_ops.ones([1, 2], name="x")
s1 = [
    (x, ("N", Ellipsis, "Q")),
]
s2 = [
    (x, "N*Q"),
]
regex = (r"Tensor .* specified shape index .*.  "
         r"Symbol `...` or `\*` for a variable number of "
         r"unspecified dimensions is only allowed as the first entry")
self.raises_static_error(shapes=s1, regex=regex)
self.raises_static_error(shapes=s2, regex=regex)
