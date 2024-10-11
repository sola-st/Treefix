# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists_test.py

def f():
    l = special_functions.tensor_list([1, 2, 3])
    directives.set_element_type(l, dtype=dtypes.int32, shape=())
    s = l.pop()
    exit((s, l))

tr = self.transform(f, (directives_converter, lists))

ts, tl = tr()
r = list_ops.tensor_list_stack(tl, dtypes.int32)
self.assertAllEqual(self.evaluate(r), [1, 2])
self.assertAllEqual(self.evaluate(ts), 3)
