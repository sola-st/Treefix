# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
scalar = array_ops.constant(5, name="rank_zero")
x = array_ops.ones([2, 2], name="x")
shapes = [(scalar, ("a",)), (x, ("a", 2))]
regex = (r"Specified by tensor .* dimension 0.  "
         r"Tensor .* dimension 0 must have size 1.  "
         r"Received size 2")
self.raises_static_error(shapes=shapes, regex=regex)
