# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring_test.py
buckets = monitoring.ExponentialBuckets(1.0, 2.0, 2)
sampler = monitoring.Sampler('test/sampler', buckets, 'test sampler')
sampler.get_cell().add(1.0)
sampler.get_cell().add(5.0)
histogram_proto = sampler.get_cell().value()
self.assertEqual(histogram_proto.min, 1.0)
self.assertEqual(histogram_proto.num, 2.0)
self.assertEqual(histogram_proto.sum, 6.0)

sampler1 = monitoring.Sampler('test/sampler1', buckets, 'test sampler',
                              'label1')
sampler1.get_cell('foo').add(2.0)
sampler1.get_cell('foo').add(4.0)
sampler1.get_cell('bar').add(8.0)
histogram_proto1 = sampler1.get_cell('foo').value()
self.assertEqual(histogram_proto1.max, 4.0)
self.assertEqual(histogram_proto1.num, 2.0)
self.assertEqual(histogram_proto1.sum, 6.0)
