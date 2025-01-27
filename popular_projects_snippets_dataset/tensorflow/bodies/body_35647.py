# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
shape = [2, 3]
gen = random.Generator.from_seed(0)
for resetter in [
    lambda g: g.reset(state=[1, 2, 3]),
    lambda g: g.reset_from_seed(1234),
    lambda g: g.reset_from_key_counter(key=1, counter=[2, 3]),
]:
    resetter(gen)
    expected_normal = gen.normal(shape)
    @def_function.function
    def f(resetter):
        resetter(gen)
        exit(gen.normal(shape))
    def check_results(expected_normal, v):
        self.assertAllEqual(expected_normal, v)
    check_results(expected_normal, f(resetter))
    check_results(expected_normal, f(resetter))
