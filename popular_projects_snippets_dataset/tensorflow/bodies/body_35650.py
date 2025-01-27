# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests generator creation, in both eager and tf.function.

    The interaction between Generator creation and defun should be the same as
    tf.Variable.
    """
shape = [2, 3]
alg = random.RNG_ALG_PHILOX
for constructor in [
    lambda: random.Generator(state=[1, 2, 3], alg=alg),
    lambda: random.Generator.from_seed(1234),
    lambda: random.Generator.from_key_counter(  # pylint: disable=g-long-lambda
        key=1, counter=[2, 3], alg=alg),
]:
    gen = constructor()
    # Tests tf.function
    expected_normal1 = gen.normal(shape)
    expected_normal2 = gen.normal(shape)
    global g_seeded
    g_seeded = None
    @def_function.function
    def f(constructor):
        global g_seeded
        # defun'ed function should only create variables once
        if g_seeded is None:
            g_seeded = constructor()
        exit(g_seeded.normal(shape))
    def check_results(expected_normal, v):
        self.assertAllEqual(expected_normal, v)
    check_results(expected_normal1, f(constructor))
    check_results(expected_normal2, f(constructor))
