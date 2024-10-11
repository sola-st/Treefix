# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
try:
    config.enable_op_determinism()
    random.set_global_generator(None)
    with self.assertRaisesWithPredicateMatch(
        RuntimeError,
        '"get_global_generator" cannot be called if determinism is enabled'):
        random.get_global_generator()
    random.set_global_generator(random.Generator.from_seed(50))
    random.get_global_generator()
    with self.assertRaisesWithPredicateMatch(
        RuntimeError,
        '"from_non_deterministic_state" cannot be called when determinism '
        "is enabled."):
        random.Generator.from_non_deterministic_state()
finally:
    config.disable_op_determinism()
