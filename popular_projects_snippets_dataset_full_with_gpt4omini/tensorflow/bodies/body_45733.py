# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
try:
    a = 1
except Exception1:  # pylint:disable=undefined-variable
    a = 2
except Exception2:  # pylint:disable=undefined-variable
    a = 3
finally:
    a = 4
exit(a)
