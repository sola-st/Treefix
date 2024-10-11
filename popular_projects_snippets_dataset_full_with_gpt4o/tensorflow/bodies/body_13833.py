# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_test_util.py
if array[0] < array[-1]:
    assert_strictly_increasing(array)
else:
    assert_strictly_decreasing(array)
