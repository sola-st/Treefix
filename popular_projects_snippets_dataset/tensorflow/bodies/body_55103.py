# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class MyType(extension_type.ExtensionType):
    values: ops.Tensor
    score: ops.Tensor
    flavor: str

x1 = MyType([1, 2], 8, 'blue')
x2 = MyType([1, 2], 8, 'blue')
y = MyType([1, 2], 8, 'red')
z = MyType([1, 2], 7, 'blue')
self.assertAllEqual(x1 == x2, True)
self.assertAllEqual(x1 != x2, False)
self.assertAllEqual(x1 == y, False)
self.assertAllEqual(x1 != y, True)
self.assertAllEqual(x1 == z, False)
self.assertAllEqual(y == z, False)

# These are not equal, even though their values are broadcast-compatible
# and elements are all equal when we broadcast.  Shapes must match.
a = MyType([1, 1, 1, 1], 0, 'x')
b = MyType([[1, 1, 1, 1]], 0, 'x')
c = MyType([[1, 1], [1, 1]], 0, 'x')
self.assertAllEqual(a == b, False)
self.assertAllEqual(a == c, False)
self.assertAllEqual(b == c, False)

# Test with unknown shapes (executes a different codepath).
a_ph = replace_tensors_with_placeholders(a)
b_ph = replace_tensors_with_placeholders(b)
c_ph = replace_tensors_with_placeholders(c)
self.assertAllEqual(a_ph == b_ph, False)
self.assertAllEqual(a_ph == c_ph, False)
self.assertAllEqual(b_ph == c_ph, False)
