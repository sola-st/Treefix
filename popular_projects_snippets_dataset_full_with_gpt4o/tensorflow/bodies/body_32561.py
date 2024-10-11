# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = array_ops.constant(2, name="x")
shapes = [
    (x, (2,)),
]
regex = (r"Specified explicitly.  "
         r"Tensor .* dimension 0 must have size 2.  "
         r"Received size 1")
self.raises_static_error(shapes=shapes, regex=regex)
