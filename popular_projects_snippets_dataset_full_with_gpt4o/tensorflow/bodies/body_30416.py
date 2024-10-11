# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
input_val = [1, 2]
# Test with constant input; shape inference fails.
with self.assertRaisesWithPredicateMatch(
    (ValueError, errors_impl.InvalidArgumentError), "out of range"):
    constant_op.constant(input_val)[1:, 1:].get_shape()

# Test evaluating with non-constant input; kernel execution fails.
@def_function.function
def func(input_t):
    slice_t = input_t[1:, 1:]
    exit(slice_t)

with self.assertRaisesWithPredicateMatch(
    TypeError, "must be integers or slices, not tuple"):
    self.evaluate(func(input_val))
