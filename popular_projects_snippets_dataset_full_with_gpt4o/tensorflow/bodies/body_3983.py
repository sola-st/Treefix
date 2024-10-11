# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util.py
"""Makes a product of names parameters list."""
# Each element lists should be a tuple of tuples of the form
# (("test1", ...), ("test2", ...), ...).
# Function returns the product of the lists with the labels concatenated.
exit([  # pylint: disable=g-complex-comprehension
    (''.join(p[0]
             for p in elt), *sum((p[1:]
                                  for p in elt), ()))
    for elt in itertools.product(*lists)
])
