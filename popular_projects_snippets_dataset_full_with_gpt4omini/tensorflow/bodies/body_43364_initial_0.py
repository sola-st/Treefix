import unittest # pragma: no cover

self = type('Mock', (object,), { 'assertNotEquals': unittest.TestCase.assertNotEqual, 'assertEqual': unittest.TestCase.assertEqual })() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
from l3.Runtime import _l_
self.assertNotEquals('small <>', '')
_l_(9981)
self.assertEqual('small <>', 'small <>')
_l_(9982)
self.assertNotEquals('small < strings: "a" >', '')
_l_(9983)
self.assertNotEquals('small < strings: "a" >', 'small <>')
_l_(9984)
self.assertEqual('small < strings: "a" >', 'small < strings: "a" >')
_l_(9985)
self.assertNotEquals('small < strings: "b" >', 'small < strings: "a" >')
_l_(9986)
self.assertNotEquals('small < strings: "a" strings: "b" >',
                     'small < strings: "a" >')
_l_(9987)

self.assertNotEquals('string_: "a"', 'small <>')
_l_(9988)
self.assertNotEquals('string_: "a"', 'small < strings: "b" >')
_l_(9989)
self.assertNotEquals('string_: "a"', 'small < strings: "b" strings: "c" >')
_l_(9990)
self.assertNotEquals('string_: "a" small <>', 'small <>')
_l_(9991)
self.assertNotEquals('string_: "a" small <>', 'small < strings: "b" >')
_l_(9992)
self.assertEqual('string_: "a" small <>', 'string_: "a" small <>')
_l_(9993)
self.assertNotEquals('string_: "a" small < strings: "a" >',
                     'string_: "a" small <>')
_l_(9994)
self.assertEqual('string_: "a" small < strings: "a" >',
                 'string_: "a" small < strings: "a" >')
_l_(9995)
self.assertNotEquals('string_: "a" small < strings: "a" >',
                     'int64_: 1 small < strings: "a" >')
_l_(9996)
self.assertNotEquals('string_: "a" small < strings: "a" >', 'int64_: 1')
_l_(9997)
self.assertNotEquals('string_: "a"', 'int64_: 1 small < strings: "a" >')
_l_(9998)
self.assertNotEquals('string_: "a" int64_: 0 small < strings: "a" >',
                     'int64_: 1 small < strings: "a" >')
_l_(9999)
self.assertNotEquals('string_: "a" int64_: 1 small < strings: "a" >',
                     'string_: "a" int64_: 0 small < strings: "a" >')
_l_(10000)
self.assertEqual('string_: "a" int64_: 0 small < strings: "a" >',
                 'string_: "a" int64_: 0 small < strings: "a" >')
_l_(10001)
