# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/kullback_leibler_test.py

class MyDist(normal.Normal):
    pass

with self.assertRaisesRegex(TypeError, "must be callable"):
    kullback_leibler.RegisterKL(MyDist, MyDist)("blah")

# First registration is OK
kullback_leibler.RegisterKL(MyDist, MyDist)(lambda a, b: None)

# Second registration fails
with self.assertRaisesRegex(ValueError, "has already been registered"):
    kullback_leibler.RegisterKL(MyDist, MyDist)(lambda a, b: None)
