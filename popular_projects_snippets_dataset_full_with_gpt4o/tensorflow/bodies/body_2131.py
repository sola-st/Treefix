# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm_test.py
# Run with all-0 weights, no padding.
o = self._RunLSTMLayer('zeros', init_ops.zeros_initializer(), 0., 0., 0.)
self.assertAllClose(o, [[[0.]] * self._batch_size] * 3)
o = self._RunLSTMLayer('zeros', init_ops.zeros_initializer(), 0., 1., 0.)
self.assertAllClose(o, [[[.25]] * self._batch_size,
                        [[.125]] * self._batch_size,
                        [[.0625]] * self._batch_size])
o = self._RunLSTMLayer('zeros', init_ops.zeros_initializer(), 1., 0., 0.)
self.assertAllClose(o, [[[0.]] * self._batch_size] * 3)
o = self._RunLSTMLayer('zeros', init_ops.zeros_initializer(), 1., 1., 0.)
self.assertAllClose(o, [[[.25]] * self._batch_size,
                        [[.125]] * self._batch_size,
                        [[.0625]] * self._batch_size])

# Run with all-1 weights, no padding.
weight1 = 1.
for m_init in [0., 1.]:
    for c_init in [0., 1.]:
        o = self._RunLSTMLayer('ones',
                               init_ops.ones_initializer(), m_init, c_init, 0.)
        m0 = self._NextM(self._inputs, weight1, m_init, c_init)
        c0 = self._NextC(self._inputs, weight1, m_init, c_init)
        self.assertAllClose(o[0], m0)
        m1 = self._NextM(self._inputs, weight1, m0, c0)
        c1 = self._NextC(self._inputs, weight1, m0, c0)
        self.assertAllClose(o[1], m1)
        m2 = self._NextM(self._inputs, weight1, m1, c1)
        self.assertAllClose(o[2], m2)

    # Run with random weights.
for weight in np.random.rand(3):
    weight_tf = constant_op.constant(weight, dtypes.float32)
    random_weight = lambda shape, w=weight_tf: array_ops.fill(shape, w)

    # No padding.
    for m_init in [0., 1.]:
        for c_init in [0., 1.]:
            o = self._RunLSTMLayer('random', random_weight, m_init, c_init, 0.)
            m0 = self._NextM(self._inputs, weight, m_init, c_init)
            c0 = self._NextC(self._inputs, weight, m_init, c_init)
            self.assertAllClose(o[0], m0)
            m1 = self._NextM(self._inputs, weight, m0, c0)
            c1 = self._NextC(self._inputs, weight, m0, c0)
            self.assertAllClose(o[1], m1)
            m2 = self._NextM(self._inputs, weight, m1, c1)
            self.assertAllClose(o[2], m2)

      # Set padding.
    o = self._RunLSTMLayer('random', random_weight, 0., 0., 1.)
    self.assertAllClose(o, [[[0.]] * self._batch_size] * 3)
    o = self._RunLSTMLayer('random', random_weight, 0., 1., 1.)
    self.assertAllClose(o, [[[0.]] * self._batch_size] * 3)
    o = self._RunLSTMLayer('random', random_weight, 1., 0., 1.)
    self.assertAllClose(o, [[[1.]] * self._batch_size] * 3)
    o = self._RunLSTMLayer('random', random_weight, 1., 1., 1.)
    self.assertAllClose(o, [[[1.]] * self._batch_size] * 3)
