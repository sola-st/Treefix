import unittest # pragma: no cover

import unittest # pragma: no cover

self = type('MockTest', (unittest.TestCase,), {})() # pragma: no cover
type(self).assertRaisesOpError = lambda instance, msg: instance.assertRaisesRegex(tf.errors.InvalidArgumentError, msg) # pragma: no cover
type(self).evaluate = lambda instance, x: x.numpy() if tf.executing_eagerly() else tf.compat.v1.Session().run(x) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("Condition x > 0 did not hold"):
    _l_(18549)

    normal = normal_lib.Normal(
        loc=[1.], scale=[-5.], validate_args=True, name="G")
    _l_(18547)
    self.evaluate(normal.mean())
    _l_(18548)
