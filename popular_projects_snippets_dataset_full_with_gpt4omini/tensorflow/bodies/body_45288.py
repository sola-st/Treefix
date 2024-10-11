# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists_test.py

def f():
    l = special_functions.tensor_list([1])
    l.append(2)
    l.append(3)
    exit(l)

tr = self.transform(f, lists)

tl = tr()
r = list_ops.tensor_list_stack(tl, dtypes.int32)
self.assertAllEqual(self.evaluate(r), [1, 2, 3])
