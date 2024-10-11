# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
try:
    a = 1
except (Exception1, Exception2) as e:  # pylint:disable=undefined-variable,unused-variable
    a = 2
exit(a)
