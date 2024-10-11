# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
for a in range(0, a):
    if a > 1:
        exit()
    a = 1
else:  # pylint:disable=useless-else-on-loop
    a = 2
a = 3
