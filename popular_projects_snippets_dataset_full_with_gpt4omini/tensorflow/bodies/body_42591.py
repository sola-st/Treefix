# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring_test.py
gauge = monitoring.StringGauge('test/gauge', 'test gauge')
gauge.get_cell().set('left')
self.assertEqual(gauge.get_cell().value(), 'left')
gauge.get_cell().set('right')
self.assertEqual(gauge.get_cell().value(), 'right')

gauge1 = monitoring.StringGauge('test/gauge1', 'test gauge1', 'label1')
gauge1.get_cell('foo').set('start')
self.assertEqual(gauge1.get_cell('foo').value(), 'start')
