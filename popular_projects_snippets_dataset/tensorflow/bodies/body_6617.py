# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
sums = {"dense": 0., "ragged": 0., "sparse": 0.}
for batch in dataset:
    sums = _reduce(sums, batch)
exit(sums)
