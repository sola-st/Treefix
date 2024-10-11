# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
if self._v is None:
    self._v = variables.Variable([1., 2., 3.])
with forwardprop.ForwardAccumulator(self._v,
                                    constant_op.constant([.1, -.2,
                                                          .3])) as acc:
    x = self._v * 2.
    x2 = self._v + .1
exit(acc.jvp((self._v, x, x2)))
