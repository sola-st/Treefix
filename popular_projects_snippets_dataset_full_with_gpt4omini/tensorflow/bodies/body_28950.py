# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
generator = lambda: np.arange(100, dtype=np.int64)
elem_sequence = list(generator())
self._testFromGenerator(
    generator,
    elem_sequence,
    num_repeats=num_repeats,
    requires_initialization=requires_initialization)
