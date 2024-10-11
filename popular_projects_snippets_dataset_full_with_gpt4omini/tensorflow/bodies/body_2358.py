# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
"""Tests that proper errors are raised.
    """
shape = [2, 3]
with ops.device(xla_device_name()):
    gen = random.Generator.from_seed(seed=1234, alg=random.RNG_ALG_THREEFRY)
    with self.assertRaisesWithPredicateMatch(
        errors_impl.InvalidArgumentError,
        r"algorithm.* must be of shape \[\], not"):
        gen_stateful_random_ops.stateful_standard_normal_v2(
            gen.state.handle, [0, 0], shape)
    with self.assertRaisesWithPredicateMatch(
        TypeError, "EagerTensor of dtype int64"):
        gen_stateful_random_ops.stateful_standard_normal_v2(
            gen.state.handle, 1.1, shape)
    with self.assertRaisesWithPredicateMatch(
        errors_impl.InvalidArgumentError,
        "Unsupported algorithm id"):
        gen_stateful_random_ops.stateful_standard_normal_v2(
            gen.state.handle, 123, shape)
    with self.assertRaisesWithPredicateMatch(errors_impl.InvalidArgumentError,
                                             "Unsupported algorithm id"):
        gen_stateful_random_ops.rng_read_and_skip(
            gen.state.handle, alg=123, delta=10)
    var = variables.Variable([0, 0], dtype=dtypes.uint32)
    with self.assertRaisesWithPredicateMatch(
        errors_impl.InvalidArgumentError,
        "Trying to read variable .* Expected int64 got"):
        gen_stateful_random_ops.stateful_standard_normal_v2(
            var.handle, random.RNG_ALG_THREEFRY, shape)
    var = variables.Variable([[0]], dtype=dtypes.int64)
    with self.assertRaisesWithPredicateMatch(
        errors_impl.InvalidArgumentError,
        "RNG state must have one and only one dimension, not"):
        gen_stateful_random_ops.stateful_standard_normal_v2(
            var.handle, random.RNG_ALG_THREEFRY, shape)
    var = variables.Variable([0], dtype=dtypes.int64)
    with self.assertRaisesWithPredicateMatch(
        errors_impl.InvalidArgumentError,
        "The size of the state must be at least"):
        gen_stateful_random_ops.stateful_standard_normal_v2(
            var.handle, random.RNG_ALG_THREEFRY, shape)
    var = variables.Variable([0, 0], dtype=dtypes.int64)
    with self.assertRaisesWithPredicateMatch(
        errors_impl.InvalidArgumentError,
        "The size of the state must be at least"):
        gen_stateful_random_ops.stateful_standard_normal_v2(
            var.handle, random.RNG_ALG_PHILOX, shape)
