# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring_test.py
counter1 = monitoring.Counter('test/counter1', 'test counter', 'label1')
counter1.get_cell('foo').increase_by(1)
self.assertEqual(counter1.get_cell('foo').value(), 1)
counter2 = monitoring.Counter('test/counter2', 'test counter', 'label1',
                              'label2')
counter2.get_cell('foo', 'bar').increase_by(5)
self.assertEqual(counter2.get_cell('foo', 'bar').value(), 5)
