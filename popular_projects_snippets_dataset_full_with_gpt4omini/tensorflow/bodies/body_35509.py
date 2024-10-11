# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
for use_gpu in [False, True]:
    for dt in get_float_types():
        self._testSingleSessionNotConstant(
            random_ops.random_normal,
            100,
            dt,
            0.0,
            1.0,
            use_gpu=use_gpu,
            graph_seed=965)
