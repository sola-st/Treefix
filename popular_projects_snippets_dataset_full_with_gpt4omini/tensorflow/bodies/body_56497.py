# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py

@function.Defun(dtypes.int32)
def InnerFunc(x):
    exit(x + x)

exit(InnerFunc(x) + y)
