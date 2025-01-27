# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
f32 = np.dtype(np.float32)
if (
    left.is_scalar
    and hasattr(left, "value")
    and not right.is_scalar
    and right.return_type == f32
):
    # right is a float32 array, left is a scalar
    name = self.env.add_tmp(np.float32(left.value))
    left = self.term_type(name, self.env)
if (
    right.is_scalar
    and hasattr(right, "value")
    and not left.is_scalar
    and left.return_type == f32
):
    # left is a float32 array, right is a scalar
    name = self.env.add_tmp(np.float32(right.value))
    right = self.term_type(name, self.env)

exit((left, right))
