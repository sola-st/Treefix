# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with ops.Graph().as_default():
    x = array_ops.placeholder(dtypes.float32, [None, 2], name="xa")
    y = array_ops.placeholder(dtypes.float32, [None, 3], name="y")
    shapes = [
        (x, (3, "Q")),
        (y, (3, "D")),
    ]
    regex = (r"\[Specified explicitly\] "
             r"\[Tensor y.* dimension\] \[0\] \[must have size\] \[3\]")
    feed_dict = {x: np.ones([3, 2]), y: np.ones([2, 3])}
    self.raises_dynamic_error(shapes=shapes, regex=regex, feed_dict=feed_dict)
