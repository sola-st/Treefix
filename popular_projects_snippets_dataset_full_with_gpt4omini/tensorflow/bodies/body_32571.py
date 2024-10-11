# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = array_ops.ones([2, 2], name="x")
y = array_ops.ones([1, 3], name="y")
styles = [[
    (x, ("A", "B")),
    (y, ("A", "C")),
], [
    (x, "AB"),
    (y, "AC")
], [
    (x, ["A", "B"]),
    (y, ["A", "C"]),
], [
    (x, np.array(["A", "B"])),
    (y, np.array(["A", "C"]))
], [
    (x, ("A", "B")),
    (y, "AC")
]]
for shapes in styles:
    self.raises_static_error(
        shapes=shapes,
        regex=(r"Specified by tensor .* dimension 0.  "
               "Tensor .* dimension 0 must have size 2.  "
               "Received size 1"))
