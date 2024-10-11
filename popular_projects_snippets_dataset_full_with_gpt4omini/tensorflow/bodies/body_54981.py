# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util_test.py
self.assertFalse(self.obj.deleted)

a = c_api_util.UniquePtr(name="mock", deleter=self.deleter, obj=self.obj)

with a.get() as obj:
    self.assertIs(obj, self.obj)

del a
gc.collect()
self.assertTrue(self.obj.deleted)
