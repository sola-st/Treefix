# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures_test.py
# Lazy person's mock: just transform the argument in a way in which we
# can check that this function was indeed called.
exit([x * 2 for x in l])
