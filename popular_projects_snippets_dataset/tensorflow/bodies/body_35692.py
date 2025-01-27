# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests that proper errors are raised.
    """
shape = [2, 3]
gen = random.Generator.from_seed(1234)
with self.assertRaisesWithPredicateMatch(
    errors.InvalidArgumentError,
    r"must have shape \[\], not"):
    gen_stateful_random_ops.stateful_standard_normal_v2(
        gen.state.handle, [0, 0], shape)
with self.assertRaisesWithPredicateMatch(
    errors.InvalidArgumentError,
    r"must have shape \[\], not"):
    gen_stateful_random_ops.rng_skip(
        gen.state.handle, gen.algorithm, [0, 0])
with self.assertRaisesWithPredicateMatch(
    TypeError, "EagerTensor of dtype int64"):
    gen_stateful_random_ops.stateful_standard_normal_v2(
        gen.state.handle, 1.1, shape)
with self.assertRaisesWithPredicateMatch(
    errors.InvalidArgumentError,
    "Unsupported algorithm id"):
    gen_stateful_random_ops.stateful_standard_normal_v2(
        gen.state.handle, 123, shape)
with self.assertRaisesWithPredicateMatch(errors.InvalidArgumentError,
                                         "Unsupported algorithm id"):
    gen_stateful_random_ops.rng_read_and_skip(
        gen.state.handle, alg=123, delta=10)
var = variables.Variable([0, 0], dtype=dtypes.int32)
with self.assertRaisesWithPredicateMatch(
    errors.InvalidArgumentError,
    "dtype of RNG state variable must be int64, not"):
    gen_stateful_random_ops.stateful_standard_normal_v2(
        var.handle, random.RNG_ALG_PHILOX, shape)
var = variables.Variable([[0]], dtype=dtypes.int64)
with self.assertRaisesWithPredicateMatch(
    errors.InvalidArgumentError,
    "RNG state must have one and only one dimension, not"):
    gen_stateful_random_ops.stateful_standard_normal_v2(
        var.handle, random.RNG_ALG_PHILOX, shape)
var = variables.Variable([0], dtype=dtypes.int64)
with self.assertRaisesWithPredicateMatch(
    errors.InvalidArgumentError,
    "For the Philox algorithm, the size of state must be at least"):
    gen_stateful_random_ops.stateful_standard_normal_v2(
        var.handle, random.RNG_ALG_PHILOX, shape)
with self.assertRaisesWithPredicateMatch(
    ValueError,
    "minval must be a scalar; got a tensor of shape "):
    @def_function.function
    def f():
        gen.uniform(shape=shape, minval=array_ops.zeros(shape, "int32"),
                    maxval=100, dtype="int32")
    f()
with self.assertRaisesWithPredicateMatch(
    ValueError,
    "maxval must be a scalar; got a tensor of shape "):
    @def_function.function
    def f2():
        gen.uniform(
            shape=shape, minval=0, maxval=array_ops.ones(shape, "int32") * 100,
            dtype="int32")
    f2()
