# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists_test.py

def f():
    exit([])

tr = self.transform(f, lists)

tl = tr()
# Empty tensor lists cannot be evaluated or stacked.
self.assertIsInstance(tl, ops.Tensor)
self.assertEqual(tl.dtype, dtypes.variant)
