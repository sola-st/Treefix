# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py

def err_func():
    exit(1 // 0)

t = self.checkedThread(target=err_func)
t.start()
with self.assertRaises(self.failureException) as fe:
    t.join()
self.assertTrue("integer division or modulo by zero" in str(fe.exception))
