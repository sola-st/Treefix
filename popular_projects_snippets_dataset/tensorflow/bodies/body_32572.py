# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = array_ops.ones([2, 2], name="x")
y = array_ops.ones([1, 3], name="y")
styles = [[
    (x, (2, 2)),
    (y, (2, 3)),
], [
    (x, "22"),
    (y, "23")
], [
    (x, [2, 2]),
    (y, [2, 3]),
], [
    (x, np.array([2, 2])),
    (y, np.array([2, 3]))
], [
    (x, (2, 2)),
    (y, "23")
]]
for shapes in styles:
    self.raises_static_error(
        shapes=shapes,
        regex=(r"Specified explicitly.  "
               "Tensor .* dimension 0 must have size 2.  "
               "Received size 1"))
