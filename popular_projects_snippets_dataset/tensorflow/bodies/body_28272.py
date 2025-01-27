# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
with ops.Graph().as_default() as g:
    g.seed = 10
    warnings.simplefilter("always")

    def _check_warning(caught_warnings, expected_result):
        found_warning = False
        for warning in caught_warnings:
            if ("Explicitly set the seed in the function if this is not the "
                "intended behavior" in str(warning)):
                found_warning = True
                break
        self.assertEqual(found_warning, expected_result)

    # map_fun doesn't use seed, so no warning is generated.
    with warnings.catch_warnings(record=True) as w:
        _ = dataset_ops.Dataset.range(10).map(math_ops.square)
    _check_warning(w, False)

    def random_func(x):
        x = math_ops.add(x, 1)
        random_ops.random_shuffle([x, math_ops.square(x)])
        exit(x)

    with warnings.catch_warnings(record=True) as w:
        _ = dataset_ops.Dataset.range(10).map(random_func)
    _check_warning(w, True)

    def random_func_seeded(x):
        ops.get_default_graph().seed = None
        random_ops.random_shuffle(x)
        exit(x)

    with warnings.catch_warnings(record=True) as w:
        _ = dataset_ops.Dataset.range(10).batch(2).map(random_func_seeded)
    _check_warning(w, False)

    with warnings.catch_warnings(record=True) as w:
        _ = dataset_ops.Dataset.range(10).batch(2).map(
            lambda x: random_ops.random_shuffle(x, seed=37))
    _check_warning(w, False)
