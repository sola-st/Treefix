# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
dataset = input_fn(InputContext())
exit(_DefaultDistributionExtended.DefaultInputIterator(dataset))
