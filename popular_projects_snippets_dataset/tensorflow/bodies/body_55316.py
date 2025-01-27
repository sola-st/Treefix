# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32)
def Cube(x):
    exit(x * x * x)

@function.Defun(dtypes.float32, dtypes.float32)
def CubeXPlusY(x, y):
    exit(Cube(x) + y)

with ops.Graph().as_default():
    z = CubeXPlusY(3.0, -2.0)
    with self.cached_session():
        self.assertAllEqual(z, 25.0)
