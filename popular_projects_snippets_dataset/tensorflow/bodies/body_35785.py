# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session():
    rnd = variables.Variable(random_ops.random_uniform([3, 6]), name="rnd")
    self.assertEqual("rnd:0", rnd.name)
    self.assertEqual([3, 6], rnd.get_shape())
    self.assertEqual([3, 6], rnd.get_shape())
    self.assertEqual([3, 6], rnd.shape)

    dep = variables.Variable(rnd.initialized_value(), name="dep")
    self.assertEqual("dep:0", dep.name)
    self.assertEqual([3, 6], dep.get_shape())
    self.assertEqual([3, 6], dep.get_shape())
    self.assertEqual([3, 6], dep.shape)

    # Currently have to set the shape manually for Add.
    added_val = rnd.initialized_value() + dep.initialized_value() + 2.0
    added_val.set_shape(rnd.get_shape())

    depdep = variables.Variable(added_val, name="depdep")
    self.assertEqual("depdep:0", depdep.name)
    self.assertEqual([3, 6], depdep.get_shape())
    self.assertEqual([3, 6], depdep.get_shape())
    self.assertEqual([3, 6], depdep.shape)

    self.evaluate(variables.global_variables_initializer())

    self.assertAllClose(self.evaluate(rnd), self.evaluate(dep))
    self.assertAllClose(
        self.evaluate(rnd) + self.evaluate(dep) + 2.0, self.evaluate(depdep))
