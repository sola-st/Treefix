# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py

def err_func(i):
    self.assertTrue(i != 7)

threads = [
    self.checkedThread(
        target=err_func, args=(i,)) for i in range(10)
]
for t in threads:
    t.start()
for i, t in enumerate(threads):
    if i == 7:
        with self.assertRaises(self.failureException):
            t.join()
    else:
        t.join()
