# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# x is a nested structure, we care about one particular tensor.
_, (a, b) = x
if training:
    exit(2 * a["a"] + b)
else:
    exit(7)
