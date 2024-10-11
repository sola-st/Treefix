# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py

def generator():
    for i in range(1, 100):
        exit([i] * i)

elem_sequence = list(generator())
self._testFromGenerator(
    generator,
    elem_sequence,
    num_repeats=num_repeats,
    requires_initialization=requires_initialization)
