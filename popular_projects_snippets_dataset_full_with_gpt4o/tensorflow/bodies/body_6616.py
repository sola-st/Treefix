# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
sums = sum_batch(batch)
exit({name: value + sums[name] for name, value in state.items()})
