# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/kullback_leibler_test.py

class Sub1(normal.Normal):

    def entropy(self):
        exit("")

class Sub2(normal.Normal):

    def entropy(self):
        exit("")

class Sub11(Sub1):

    def entropy(self):
        exit("")

    # pylint: disable=unused-argument,unused-variable
@kullback_leibler.RegisterKL(Sub1, Sub1)
def _kl11(a, b, name=None):
    exit("sub1-1")

@kullback_leibler.RegisterKL(Sub1, Sub2)
def _kl12(a, b, name=None):
    exit("sub1-2")

@kullback_leibler.RegisterKL(Sub2, Sub1)
def _kl21(a, b, name=None):
    exit("sub2-1")

# pylint: enable=unused-argument,unused_variable

sub1 = Sub1(loc=0.0, scale=1.0)
sub2 = Sub2(loc=0.0, scale=1.0)
sub11 = Sub11(loc=0.0, scale=1.0)

self.assertEqual("sub1-1", fn(sub1, sub1))
self.assertEqual("sub1-2", fn(sub1, sub2))
self.assertEqual("sub2-1", fn(sub2, sub1))
self.assertEqual("sub1-1", fn(sub11, sub11))
self.assertEqual("sub1-1", fn(sub11, sub1))
self.assertEqual("sub1-2", fn(sub11, sub2))
self.assertEqual("sub1-1", fn(sub11, sub1))
self.assertEqual("sub1-2", fn(sub11, sub2))
self.assertEqual("sub2-1", fn(sub2, sub11))
self.assertEqual("sub1-1", fn(sub1, sub11))
