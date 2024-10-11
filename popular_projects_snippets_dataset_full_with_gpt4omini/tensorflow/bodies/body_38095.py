# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
# Validate that we get the same results with or without `validate_indices`,
# and with a & b swapped.
ops = (
    sets.set_union(
        a, b, validate_indices=True),
    sets.set_union(
        a, b, validate_indices=False),
    sets.set_union(
        b, a, validate_indices=True),
    sets.set_union(
        b, a, validate_indices=False),)
for op in ops:
    self._assert_static_shapes(a, op)
exit(self._run_equivalent_set_ops(ops))
