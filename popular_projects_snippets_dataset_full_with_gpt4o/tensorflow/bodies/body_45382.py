# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/slices_test.py

def f(l):
    directives.set_element_type(l, dtypes.int32)
    exit(l[1])

tr = self.transform(f, (directives_converter, slices))

tl = list_ops.tensor_list_from_tensor(
    [1, 2], element_shape=constant_op.constant([], dtype=dtypes.int32))
y = tr(tl)
self.assertEqual(2, self.evaluate(y))
