# Extracted from ./data/repos/tensorflow/tensorflow/python/util/fast_module_type_test.py
module = ChildFastModule("test")
# At first "bar" does not exist in the module's attributes
self.assertFalse(module._fastdict_key_in("bar"))
with self.assertRaisesRegex(KeyError, "module has no attribute 'bar'"):
    module._fastdict_get("bar")

module._fastdict_insert("bar", 1)
# After _fastdict_insert() the attribute is added.
self.assertTrue(module._fastdict_key_in("bar"))
self.assertEqual(1, module.bar)
