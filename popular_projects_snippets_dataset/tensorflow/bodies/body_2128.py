# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm_test.py
# Run with all-0 weights, no padding.
m, c = self._RunLSTMCell('zeros', init_ops.zeros_initializer(), 0., 0., 0.)
self.assertAllClose(m, [[0.]] * self._batch_size)
self.assertAllClose(c, [[0.]] * self._batch_size)
m, c = self._RunLSTMCell('zeros', init_ops.zeros_initializer(), 0., 1., 0.)
self.assertAllClose(m, [[.25]] * self._batch_size)
self.assertAllClose(c, [[.5]] * self._batch_size)
m, c = self._RunLSTMCell('zeros', init_ops.zeros_initializer(), 1., 0., 0.)
self.assertAllClose(m, [[.0]] * self._batch_size)
self.assertAllClose(c, [[.0]] * self._batch_size)
m, c = self._RunLSTMCell('zeros', init_ops.zeros_initializer(), 1., 1., 0.)
self.assertAllClose(m, [[.25]] * self._batch_size)
self.assertAllClose(c, [[.5]] * self._batch_size)

# Run with all-1 weights, no padding.
for m_prev in [0., 1.]:
    for c_prev in [0., 1.]:
        m, c = self._RunLSTMCell('ones',
                                 init_ops.ones_initializer(), m_prev, c_prev,
                                 0.)
        self.assertAllClose(m, self._NextM(self._inputs, 1., m_prev, c_prev))
        self.assertAllClose(c, self._NextC(self._inputs, 1., m_prev, c_prev))

    # Run with random weights.
for weight in np.random.rand(3):
    weight_tf = constant_op.constant(weight, dtypes.float32)
    random_weight = lambda shape, w=weight_tf: array_ops.fill(shape, w)

    # No padding.
    for m_prev in [0., 1.]:
        for c_prev in [0., 1.]:
            m, c = self._RunLSTMCell('random', random_weight, m_prev, c_prev, 0.)
            self.assertAllClose(m,
                                self._NextM(self._inputs, weight, m_prev, c_prev))
            self.assertAllClose(c,
                                self._NextC(self._inputs, weight, m_prev, c_prev))

      # Set padding.
    for m_prev in [0., 1.]:
        for c_prev in [0., 1.]:
            m, c = self._RunLSTMCell('random', random_weight, m_prev, c_prev, 1.)
            self.assertAllClose(m, [[m_prev]] * self._batch_size)
            self.assertAllClose(c, [[c_prev]] * self._batch_size)
