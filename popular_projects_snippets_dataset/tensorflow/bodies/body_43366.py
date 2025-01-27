# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
"""Tests that different fields are ordered by tag number.

    For reference, here are the relevant tag numbers from compare_test.proto:
      optional string string_ = 1;
      optional int64 int64_ = 2;
      optional float float_ = 3;
      optional Small small = 8;
      optional Medium medium = 7;
      optional Small small = 8;
    """
self.assertNotEquals('string_: "a"                      ',
                     '             int64_: 1            ')
self.assertNotEquals('string_: "a" int64_: 2            ',
                     '             int64_: 1            ')
self.assertNotEquals('string_: "b" int64_: 1            ',
                     'string_: "a" int64_: 2            ')
self.assertEqual('string_: "a" int64_: 1            ',
                 'string_: "a" int64_: 1            ')
self.assertNotEquals('string_: "a" int64_: 1 float_: 0.0',
                     'string_: "a" int64_: 1            ')
self.assertEqual('string_: "a" int64_: 1 float_: 0.0',
                 'string_: "a" int64_: 1 float_: 0.0')
self.assertNotEquals('string_: "a" int64_: 1 float_: 0.1',
                     'string_: "a" int64_: 1 float_: 0.0')
self.assertNotEquals('string_: "a" int64_: 2 float_: 0.0',
                     'string_: "a" int64_: 1 float_: 0.1')
self.assertNotEquals('string_: "a"                      ',
                     '             int64_: 1 float_: 0.1')
self.assertNotEquals('string_: "a"           float_: 0.0',
                     '             int64_: 1            ')
self.assertNotEquals('string_: "b"           float_: 0.0',
                     'string_: "a" int64_: 1            ')

self.assertNotEquals('string_: "a"', 'small < strings: "a" >')
self.assertNotEquals('string_: "a" small < strings: "a" >',
                     'small < strings: "b" >')
self.assertNotEquals('string_: "a" small < strings: "b" >',
                     'string_: "a" small < strings: "a" >')
self.assertEqual('string_: "a" small < strings: "a" >',
                 'string_: "a" small < strings: "a" >')

self.assertNotEquals('string_: "a" medium <>',
                     'string_: "a" small < strings: "a" >')
self.assertNotEquals('string_: "a" medium < smalls <> >',
                     'string_: "a" small < strings: "a" >')
self.assertNotEquals('medium <>', 'small < strings: "a" >')
self.assertNotEquals('medium <> small <>', 'small < strings: "a" >')
self.assertNotEquals('medium < smalls <> >', 'small < strings: "a" >')
self.assertNotEquals('medium < smalls < strings: "a" > >',
                     'small < strings: "b" >')
