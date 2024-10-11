# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
# Get ones in shape of diag, which is [B1,...,Bb, N]
# Also get the size of the diag, "N".
if self.shape.is_fully_defined():
    diag_shape = self.shape[:-1]
    diag_size = self.domain_dimension.value
else:
    diag_shape = self.shape_tensor()[:-1]
    diag_size = self.domain_dimension_tensor()
ones_diag = array_ops.ones(diag_shape, dtype=self.dtype)

# As proved in comments in self._trace, the value on the diag is constant,
# repeated N times.  This value is the trace divided by N.

# The handling of self.shape = (0, 0) is tricky, and is the reason we choose
# to compute trace and use that to compute diag_part, rather than computing
# the value on the diagonal ("diag_value") directly.  Both result in a 0/0,
# but in different places, and the current method gives the right result in
# the end.

# Here, if self.shape = (0, 0), then self.trace() = 0., and then
# diag_value = 0. / 0. = NaN.
diag_value = self.trace() / math_ops.cast(diag_size, self.dtype)

# If self.shape = (0, 0), then ones_diag = [] (empty tensor), and then
# the following line is NaN * [] = [], as needed.
exit(diag_value[..., array_ops.newaxis] * ones_diag)
