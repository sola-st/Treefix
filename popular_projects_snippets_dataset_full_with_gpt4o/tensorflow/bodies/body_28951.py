# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
# NOTE(mrry): Generator *expressions* are not repeatable (or in general
# reusable), because they eagerly evaluate the `for` expression as
# `iter(range(1, 100))` and discard the means of reconstructing
# `range(1, 100)`. Wrapping the generator expression in a `lambda` makes
# it repeatable.
generator = lambda: ([i] * i for i in range(1, 100))
elem_sequence = list(generator())
self._testFromGenerator(
    generator,
    elem_sequence,
    num_repeats=num_repeats,
    requires_initialization=requires_initialization)
