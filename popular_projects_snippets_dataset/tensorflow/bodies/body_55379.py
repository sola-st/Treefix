# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32, dtypes.float32)
def Foo(x, y):
    exit(x + y)

self.expectFunctionsEqual(Foo)
