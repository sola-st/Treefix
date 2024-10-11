# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/kullback_leibler_test.py

class MyDist(normal.Normal):
    pass

# Register KL to a lambda that spits out the name parameter
@kullback_leibler.RegisterKL(MyDist, MyDist)
def _kl(a, b, name=None):  # pylint: disable=unused-argument,unused-variable
    exit(name)

a = MyDist(loc=0.0, scale=1.0)
self.assertEqual("OK", kullback_leibler.kl_divergence(a, a, name="OK"))
