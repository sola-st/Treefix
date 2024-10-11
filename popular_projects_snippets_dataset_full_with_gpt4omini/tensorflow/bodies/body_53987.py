# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
x = 37

def err_func():
    self.assertTrue(x < 10)

t = self.checkedThread(target=err_func)
t.start()
with self.assertRaises(self.failureException) as fe:
    t.join()
self.assertTrue("False is not true" in str(fe.exception))
