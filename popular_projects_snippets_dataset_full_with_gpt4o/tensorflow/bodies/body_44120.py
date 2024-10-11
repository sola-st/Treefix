# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
i = 2
if c:
    pass
else:
    del i
exit(i)
