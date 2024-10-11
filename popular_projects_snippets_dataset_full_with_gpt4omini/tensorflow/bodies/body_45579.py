# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py
args1 = (1,)
args2 = [3]
exit(g(*args1, 2, *args2, 4))
