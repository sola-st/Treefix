# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/registry_test.py
myreg = registry.Registry('testRegistry')
with self.assertRaises(LookupError):
    myreg.lookup('testKey')
myreg.register(candidate)
self.assertEqual(myreg.lookup(candidate.__name__), candidate)
myreg.register(candidate, 'testKey')
self.assertEqual(myreg.lookup('testKey'), candidate)
self.assertEqual(
    sorted(myreg.list()), sorted(['testKey', candidate.__name__]))
