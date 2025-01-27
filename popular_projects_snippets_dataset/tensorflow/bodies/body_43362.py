# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
self.assertNotEquals('string_: "a"', '')
self.assertEqual('string_: "a"', 'string_: "a"')
self.assertNotEquals('string_: "b"', 'string_: "a"')
self.assertNotEquals('string_: "ab"', 'string_: "aa"')

self.assertNotEquals('int64_: 0', '')
self.assertEqual('int64_: 0', 'int64_: 0')
self.assertNotEquals('int64_: -1', '')
self.assertNotEquals('int64_: 1', 'int64_: 0')
self.assertNotEquals('int64_: 0', 'int64_: -1')

self.assertNotEquals('float_: 0.0', '')
self.assertEqual('float_: 0.0', 'float_: 0.0')
self.assertNotEquals('float_: -0.1', '')
self.assertNotEquals('float_: 3.14', 'float_: 0')
self.assertNotEquals('float_: 0', 'float_: -0.1')
self.assertEqual('float_: -0.1', 'float_: -0.1')

self.assertNotEquals('bool_: true', '')
self.assertNotEquals('bool_: false', '')
self.assertNotEquals('bool_: true', 'bool_: false')
self.assertEqual('bool_: false', 'bool_: false')
self.assertEqual('bool_: true', 'bool_: true')

self.assertNotEquals('enum_: A', '')
self.assertNotEquals('enum_: B', 'enum_: A')
self.assertNotEquals('enum_: C', 'enum_: B')
self.assertEqual('enum_: C', 'enum_: C')
