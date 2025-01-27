# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring_test.py
gauge = monitoring.BoolGauge('test/gauge', 'test gauge')
gauge.get_cell().set(True)
self.assertTrue(gauge.get_cell().value())
gauge.get_cell().set(False)
self.assertFalse(gauge.get_cell().value())

gauge1 = monitoring.BoolGauge('test/gauge1', 'test gauge1', 'label1')
gauge1.get_cell('foo').set(True)
self.assertTrue(gauge1.get_cell('foo').value())
