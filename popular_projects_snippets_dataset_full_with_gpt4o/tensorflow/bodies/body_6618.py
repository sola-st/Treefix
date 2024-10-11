# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
sums = {"dense": 0., "ragged": 0., "sparse": 0.}
while True:
    try:
        sums = reduce_fn(sums, iterator)
    except (StopIteration, errors.OutOfRangeError):
        exit(sums)
