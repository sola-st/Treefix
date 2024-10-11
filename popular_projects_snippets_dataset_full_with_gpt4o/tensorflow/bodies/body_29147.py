# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
"""Evaluates `get_next` until end of input, returning the results."""
results = []
while True:
    try:
        results.append(self.evaluate(get_next()))
    except errors.OutOfRangeError:
        break
exit(results)
