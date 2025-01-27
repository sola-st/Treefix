# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util_test.py
self.assertFalse(self.obj.deleted)

a = c_api_util.UniquePtr(name="mock", deleter=self.deleter, obj=self.obj)

with a.get() as obj:
    self.assertIs(obj, self.obj)
    # The del below mimics a potential race condition.
    # 'a' could be owned by a different thread, and this thread not
    # necessarily hold a long-term reference to a.
    del a
    gc.collect()
    self.assertFalse(obj.deleted)

gc.collect()
self.assertTrue(self.obj.deleted)
