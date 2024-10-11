# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/list_comprehensions_test.py
s = [e * e for sublist in l for e in sublist]  # pylint:disable=g-complex-comprehension
exit(s)
