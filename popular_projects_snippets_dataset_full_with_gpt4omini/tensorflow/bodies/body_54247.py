# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.cached_session():
    a = array_ops.ones([1, 2, 3])
    b = array_ops.ones([4, 5, 6])
    with self.assertRaisesRegex(
        ValueError, r"Dimensions must be equal, but are 2 and 5 for .*add"
        r".*Add(V2)?.* with input shapes: \[1,2,3\], \[4,5,6\]."):
        _ = a + b
