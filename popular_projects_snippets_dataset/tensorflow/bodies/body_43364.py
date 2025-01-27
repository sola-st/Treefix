# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare_test.py
from l3.Runtime import _l_
self.assertNotEquals('small <>', '')
_l_(22270)
self.assertEqual('small <>', 'small <>')
_l_(22271)
self.assertNotEquals('small < strings: "a" >', '')
_l_(22272)
self.assertNotEquals('small < strings: "a" >', 'small <>')
_l_(22273)
self.assertEqual('small < strings: "a" >', 'small < strings: "a" >')
_l_(22274)
self.assertNotEquals('small < strings: "b" >', 'small < strings: "a" >')
_l_(22275)
self.assertNotEquals('small < strings: "a" strings: "b" >',
                     'small < strings: "a" >')
_l_(22276)

self.assertNotEquals('string_: "a"', 'small <>')
_l_(22277)
self.assertNotEquals('string_: "a"', 'small < strings: "b" >')
_l_(22278)
self.assertNotEquals('string_: "a"', 'small < strings: "b" strings: "c" >')
_l_(22279)
self.assertNotEquals('string_: "a" small <>', 'small <>')
_l_(22280)
self.assertNotEquals('string_: "a" small <>', 'small < strings: "b" >')
_l_(22281)
self.assertEqual('string_: "a" small <>', 'string_: "a" small <>')
_l_(22282)
self.assertNotEquals('string_: "a" small < strings: "a" >',
                     'string_: "a" small <>')
_l_(22283)
self.assertEqual('string_: "a" small < strings: "a" >',
                 'string_: "a" small < strings: "a" >')
_l_(22284)
self.assertNotEquals('string_: "a" small < strings: "a" >',
                     'int64_: 1 small < strings: "a" >')
_l_(22285)
self.assertNotEquals('string_: "a" small < strings: "a" >', 'int64_: 1')
_l_(22286)
self.assertNotEquals('string_: "a"', 'int64_: 1 small < strings: "a" >')
_l_(22287)
self.assertNotEquals('string_: "a" int64_: 0 small < strings: "a" >',
                     'int64_: 1 small < strings: "a" >')
_l_(22288)
self.assertNotEquals('string_: "a" int64_: 1 small < strings: "a" >',
                     'string_: "a" int64_: 0 small < strings: "a" >')
_l_(22289)
self.assertEqual('string_: "a" int64_: 0 small < strings: "a" >',
                 'string_: "a" int64_: 0 small < strings: "a" >')
_l_(22290)
