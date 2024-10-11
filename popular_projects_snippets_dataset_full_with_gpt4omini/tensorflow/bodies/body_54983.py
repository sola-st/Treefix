# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util_test.py
self.assertFalse(self.obj.deleted)

a = c_api_util.UniquePtr(name="mock", deleter=self.deleter, obj=self.obj)

# The __del__ below mimics a partially started deletion, potentially
# started from another thread.
# 'a' could be owned by a different thread, and this thread not
# necessarily hold a long-term reference to a.
a.__del__()
self.assertTrue(self.obj.deleted)

with self.assertRaisesRegex(c_api_util.AlreadyGarbageCollectedError,
                            "MockClass"):
    with a.get():
        pass

gc.collect()
self.assertTrue(self.obj.deleted)
