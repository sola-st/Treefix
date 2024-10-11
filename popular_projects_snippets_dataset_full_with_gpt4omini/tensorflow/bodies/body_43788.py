# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/datasets_test.py
itr = iter(ds)
exit(10 * next(itr) + next(itr))
