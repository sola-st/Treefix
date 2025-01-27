# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
self.assertNotEquals('medium <>', '')
self.assertEqual('medium <>', 'medium <>')
self.assertNotEquals('medium < smalls <> >', 'medium <>')
self.assertEqual('medium < smalls <> >', 'medium < smalls <> >')
self.assertNotEquals('medium < smalls <> smalls <> >',
                     'medium < smalls <> >')
self.assertEqual('medium < smalls <> smalls <> >',
                 'medium < smalls <> smalls <> >')

self.assertNotEquals('medium < int32s: 0 >', 'medium < smalls <> >')

self.assertNotEquals('medium < smalls < strings: "a"> >',
                     'medium < smalls <> >')
