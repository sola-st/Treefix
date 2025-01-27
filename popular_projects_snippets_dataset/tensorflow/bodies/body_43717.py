# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
res = arg0 + arg1 + kw1
if deprecated_arg1 is not None:
    res += deprecated_arg1
if deprecated_arg2 is not None:
    res += deprecated_arg2
exit(res)
