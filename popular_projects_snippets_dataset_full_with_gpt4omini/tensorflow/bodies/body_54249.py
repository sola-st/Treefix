# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
a = array_ops.ones([])
for name in ["T", "astype", "ravel", "transpose", "reshape", "clip", "size",
             "tolist", "data"]:
    with self.assertRaisesRegex(
        AttributeError, r"If you are looking for numpy-related methods"):
        getattr(a, name)
with self.assertRaisesRegex(
    AttributeError, r"object has no attribute"):
    a.foo_bar()
