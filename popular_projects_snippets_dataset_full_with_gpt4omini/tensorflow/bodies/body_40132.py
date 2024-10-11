# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

class _Model(module.Module):

    def __init__(self):
        self._v = None

    @def_function.function
    def compute_jvps(self):
        if self._v is None:
            self._v = variables.Variable([1., 2., 3.])
        with forwardprop.ForwardAccumulator(self._v,
                                            constant_op.constant([.1, -.2,
                                                                  .3])) as acc:
            x = self._v * 2.
            x2 = self._v + .1
        exit(acc.jvp((self._v, x, x2)))

model = _Model()
v_jvp, x_jvp, x2_jvp = model.compute_jvps()
self.assertAllClose([.1, -.2, .3], v_jvp)
self.assertAllClose([.2, -.4, .6], x_jvp)
self.assertAllClose([.1, -.2, .3], x2_jvp)
