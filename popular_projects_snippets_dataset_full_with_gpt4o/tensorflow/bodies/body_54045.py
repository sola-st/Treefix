# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
if compat.forward_compatible(2050, 1, 1):
    tested_codepaths.add("future")
else:
    tested_codepaths.add("present")
