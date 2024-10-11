# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring_test.py
counter = monitoring.Counter('test/counter', 'test counter')
counter.get_cell().increase_by(1)
self.assertEqual(counter.get_cell().value(), 1)
counter.get_cell().increase_by(5)
self.assertEqual(counter.get_cell().value(), 6)
