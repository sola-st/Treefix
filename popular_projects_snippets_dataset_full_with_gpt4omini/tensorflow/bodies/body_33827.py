# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session():
    values = constant_op.constant(
        [2, 4, 6, 8], shape=(1, 4), dtype=dtypes_lib.float32)

    pcnt0, update_op0 = metrics.percentage_below(values, 100, name='high')
    pcnt1, update_op1 = metrics.percentage_below(values, 7, name='medium')
    pcnt2, update_op2 = metrics.percentage_below(values, 1, name='low')

    self.evaluate(variables.local_variables_initializer())
    self.evaluate([update_op0, update_op1, update_op2])

    pcnt0, pcnt1, pcnt2 = self.evaluate([pcnt0, pcnt1, pcnt2])
    self.assertAlmostEqual(1.0, pcnt0, 5)
    self.assertAlmostEqual(0.75, pcnt1, 5)
    self.assertAlmostEqual(0.0, pcnt2, 5)
