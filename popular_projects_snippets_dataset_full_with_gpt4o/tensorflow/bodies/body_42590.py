# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring_test.py
gauge = monitoring.IntGauge('test/gauge', 'test gauge')
gauge.get_cell().set(1)
self.assertEqual(gauge.get_cell().value(), 1)
gauge.get_cell().set(5)
self.assertEqual(gauge.get_cell().value(), 5)

gauge1 = monitoring.IntGauge('test/gauge1', 'test gauge1', 'label1')
gauge1.get_cell('foo').set(2)
self.assertEqual(gauge1.get_cell('foo').value(), 2)
