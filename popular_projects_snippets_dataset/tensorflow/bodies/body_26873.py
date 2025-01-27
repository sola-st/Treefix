# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_parallelization_test.py
name, function, should_optimize = y
exit(x + combinations.combine(
    function=combinations.NamedObject(name, function),
    should_optimize=should_optimize))
