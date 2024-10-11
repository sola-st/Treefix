# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists_test.py

def f():
    exit([1, 2, 3])

tr = self.transform(f, lists)

self.assertAllEqual(tr(), [1, 2, 3])
