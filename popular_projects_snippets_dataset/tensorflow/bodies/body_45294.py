# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists_test.py

def f():
    l = [1, 2, 3]
    exit(array_ops.stack(l))

tr = self.transform(f, lists)

self.assertAllEqual(self.evaluate(tr()), [1, 2, 3])
